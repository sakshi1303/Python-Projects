import multiprocessing

result = []

def calc_sq(num, q):
    global result
    for n in num:
        q.put(n*n)

if __name__ == "__main__":
    
    arr = [2,3,5]
    
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_sq, args=(arr, q))
    
    
    p1.start()
    p1.join()
    
    while q.empty() is False:
        print(q.get())
    