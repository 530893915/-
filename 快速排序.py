#coding:utf8

def quick_sort(array, left, right):
    if left >= right:
        return array
    low = left
    high = right
    key = array[low]
    print(array)
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        print("1:",array)
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
        print("2:",array)
        print("----------")
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)
    return array


A = [3,7,5,2,3,1]
print(quick_sort(A,0,5))
