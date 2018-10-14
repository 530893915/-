#coding:utf8

def subblt_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li)-i-1):
            print('i:',i,'j:',j)
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                print(li)
    return li
# data = input("请输入：").split(",")
# data1 = [int(i) for i in data]
# subblt_sort(data1)
# print(data1)

li = [84, 83, 88, 87, 61, 50, 70, 60, 80]
print(subblt_sort(li))


