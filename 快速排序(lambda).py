#coding:utf8

array = [84,83,88,87,61,50,70,60,80,99]

quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
    [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
    [item for item in array[1:] if item > array[0]])

print(quick_sort(array))