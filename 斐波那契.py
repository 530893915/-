#coding:utf8

# 求斐波那契数列下标为n的元素
def func(n):
    if n <= 1:
        return 1
    else:
        return func(n-1) + func(n-2)

print(func(4))