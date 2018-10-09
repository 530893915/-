#coding:utf8

def subblt_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li
# data = input("请输入：").split(",")
# data1 = [int(i) for i in data]
# subblt_sort(data1)
# print(data1)

li = [3,1,5,7,2,1,4]
print(subblt_sort(li))


