#coding:utf8

class LNode:
    def __init__(self):
        self.data = None
        self.next = None

"""
方法功能：对不带头结点的单链表进行逆序
输入参数：firstRef:链表头结点
"""
def RecursiveReverse(head):
    # 如果链表为空或者链表中只有一个元素
    if head is None or head.next is None:
        return head
    else:
        # 反转后面的结点
        newhead = RecursiveReverse(head.next)
        # 把当前遍历的结点加到后面结点逆序后链表的尾部
        head.next.next = head
        head.next = None
    return newhead

"""
方法功能：对带头结点的单链表进行逆序
输入参数：head:链表头结点
"""
def Reverse(head):
    if head is None:
        return
    # 获取链表第一个结点
    firstNode = head.next
    # 对链表进行逆序
    newhead = RecursiveReverse(firstNode)
    # 头结点指向逆序后链表的第一个结点
    head.next = newhead
    return newhead


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