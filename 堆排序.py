#coding:utf8

# 堆排序：是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

# 将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
# 将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
# 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。

# def adjust_heap(lists,i,size):
#     lchild = 2 * i + 1
#     rchild = 2 * i + 2
#     maxs = i
#     if i < size // 2:
#         if lchild < size and lists[lchild] > lists[maxs]:
#             maxs = lchild
#         if lchild < size and lists[rchild] > lists[maxs]:
#             maxs = rchild
#         if maxs != i:
#             lists[maxs],lists[i] = lists[i],lists[maxs]
#             adjust_heap(lists,maxs,size)
#
# def build_heap(lists,size):
#     for i in range(0,(size//2))[::-1]:
#         adjust_heap(lists,i,size)
#
# def heap_sort(lists):
#     size = len(lists)
#     build_heap(lists,size)
#     for i in range(0,size)[::-1]:
#         lists[0],lists[i] = lists[i],lists[0]
#         adjust_heap(lists,0,i)

def MAX_Heapify(heap,HeapSize,root):#在堆中做结构调整使得父节点的值大于子节点

    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap, HeapSize, larger)

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)#将堆的长度当独拿出来方便
    for i in range((HeapSize -2)//2,-1,-1):#从后往前出数
        MAX_Heapify(heap,HeapSize,i)

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    return heap



lists = [3,4,2,8,9,5,1]
print(HeapSort(lists))
