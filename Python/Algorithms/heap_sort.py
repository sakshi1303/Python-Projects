print('HEAP SORT!!!')
print('Enter the number of elements: ')
n = int(input())
print('Enter the array:')
arr = [int(input()) for i in range(n)]
print('Array is : ' + str(arr))
def heapify(arr, n, i):
    max = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and arr[l] > arr[max]:
        max = l
    if r < n and arr[r] > arr[max]:
        max = r
    if max != i:
        arr[i], arr[max] = arr[max], arr[i]
        heapify(arr, n, max)
    print('Intermiate elements:' + str(arr))
def max_heap(arr, n):
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
max_heap(arr, n)
print('Sorted Array is :' + str(arr))