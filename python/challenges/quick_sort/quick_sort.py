def quick_sort(arr, left, right):
    if left < right:
        pivot_point = partition(arr, left, right)
        quick_sort(arr, left, pivot_point - 1)
        quick_sort(arr, pivot_point + 1, right)
    return arr

def partition(arr, left, right):
    pivot_compare = arr[right]
    low = left - 1
    for i in range(left, right):
        if arr[i] <= pivot_compare:
            low+=1
            swap(arr, i, low)
    swap(arr, right, low + 1)
    return low + 1

def swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
