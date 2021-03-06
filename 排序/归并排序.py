#coding:utf8

# 归并排序：归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。

# 把长度为n的输入序列分成两个长度为n/2的子序列；
# 对这两个子序列分别采用归并排序；
# 将两个排序好的子序列合并成一个最终的排序序列。

def merge_sort(lists):
    if len(lists)<=1:
        return lists
    num = len(lists)//2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left,right)

def merge(left,right):
    i,j = 0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result



lists = [84, 83, 88, 87, 61, 50, 70, 60, 80]
print(merge_sort(lists))