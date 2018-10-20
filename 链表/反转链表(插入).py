#coding:utf8

class LNode:
    def __init__(self):
        self.data = None
        self.next = None

def Reverse(head):
    # 判断链表是否为空
    if head is None or head.next is None:
        return
    cur = None # 当前结点
    next = None # 后继结点
    cur = head.next.next
    # 设置链表第一个结点为尾结点
    head.next.next = None
    # 把遍历到的结点插入到头结点的后面
    while cur is not None:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next


if __name__ == '__main__':
    i = 1
    # 链表头结点
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    # 构造单链表
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print("逆序前：")
    cur = head.next
    while cur != None:
        print(cur.data)
        cur = cur.next
    print("逆序后：")
    Reverse(head)
    cur = head.next
    while cur != None:
        print(cur.data)
        cur = cur.next

# 时间复杂度：O(N)
# 空间复杂度：O(1)