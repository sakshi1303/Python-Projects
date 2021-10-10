import multiprocessing


def calc_sq(num, result, v):
    v.value = 5.67
    for idx, n in enumerate(num):
        result[idx] = n*n

if __name__ == "__main__":
    
    arr = [2,3,5]
    result= multiprocessing.Array('i', 3)
    v = multiprocessing.Value('d', 0.0)
    p1 = multiprocessing.Process(target=calc_sq, args=(arr, result, v))
    
    p1.start()
    p1.join()
    
    print(result[:])
    print(v.value)