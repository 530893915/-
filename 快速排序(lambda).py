#coding:utf8

quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
    [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
    [item for item in array[1:] if item > array[0]])

