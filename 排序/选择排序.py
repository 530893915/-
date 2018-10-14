#coding:utf8

# 选择排序：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。 

# 这里演示从小到大排序
def selection_sort(array):
    l = len(array)
    for i in range(l-1):
        minNum = i
        for j in range(i+1,l):
            if array[j] < array[minNum]:
                minNum = j
        array[i],array[minNum] = array[minNum],array[i]
    return array

array = [3,1,5,7,2,1,4]
print(selection_sort(array))