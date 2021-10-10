print('Merge Sort..')
print('Enter the no of elements in array : ')
n = int(input())
print('Enter the array : ')
arr = []
for i in range(n):
    arr.append(int(input()))
print('Array is = '+ str(arr))
def merge_sort(arr, left, right):
     if left < right:
         mid = int((left + right)//2)
         print('left = ' + str(left))
         print('mid =' + str(mid))
         print('right = '+ str(right))
         merge_sort(arr, left, mid)
         merge_sort(arr, mid + 1, right)
         merge(arr, left, mid, right)
def merge(arr, left, mid, right):
    #print('Current Array = ' + str(arr))
    left_arr = arr[left:mid+1]
    print('Left Array = ' + str(left_arr))
    right_arr = arr[mid+1:right+1]
    print('Right Array = ' + str(right_arr))
    i = 0
    j = 0
    k = left
    while(i < len(left_arr) and j < len(right_arr)):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i = i + 1
        else:
            arr[k] = right_arr[j]
            j = j + 1
        k = k + 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i = i + 1
        k = k + 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j = j + 1
        k = k + 1
    print('Merging = ' + str(arr[left:k]))
left = 0
right = n-1        
merge_sort(arr, left, right)
print('Sorted Array is :' + str(arr))
