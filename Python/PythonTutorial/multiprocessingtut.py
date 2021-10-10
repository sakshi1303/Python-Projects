import time
import multiprocessing


square_result = []
def calc_sq(num):
    print('Square..')
    for n in num:
        ##time.sleep(5)
        print('square:' +  str(n*n))
        square_result.append(n*n)
    print('within a process result ' + str(square_result))    
        
def calc_cb(num):
    for n in num:
        time.sleep(5)
        print('cube:' + str(n*n*n))

if __name__ == "__main__":
    arr = [2,3,8,9]
    print('Hello')
    p1 = multiprocessing.Process(target=calc_sq, args=(arr,))
    ##p2 = multiprocessing.Process(target=calc_cb, args=(arr,))
    
    p1.start()
    ##p2.start()
    
    p1.join()
    ##p2.join()
    
    print('result ' + str(square_result))
    print("Done!")