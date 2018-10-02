#coding:utf8

def subblt_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                print(i,j,li)
            else:
                print(i,j,li)

data = input("请输入：").split(",")
data1 = [int(i) for i in data]
subblt_sort(data1)
print(data1)


