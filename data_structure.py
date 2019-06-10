
"""
反转单向链表
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    pre = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node
    return pre


def gen_list(iterable):
    pre, head = None, None
    for i in iterable:
        node = ListNode(i)
        if not head:
            head = node
        if pre:
            pre.next = node
        pre = node
    return head


def print_list(head):
    while head:
        print(head.val, end=', ')
        head = head.next
    print()

"""
实现队列
"""
from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def append(self, v):
        self.items.append(v)

    def pop(self):
        return self.items.popleft()

    def __len__(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = deque()

    def append(self, v):
        self.items.append(v)

    def pop(self):
        return self.items.pop()


import heapq

class TopK:
    """
    获取大量元素 topK 大个元素，固定内存
    思路：
        先放入前 K 个，建立最小堆
        剩余元素继续迭代：
            if 当前元素 < 堆顶元素：跳过（肯定不是前 K 大）
            else：替换堆顶为当前元素，调整堆
    """
    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable

    def push(self, v):
        if len(self.minheap) >= self.capacity:  # 堆满
            min_val = self.minheap[0]
            if v < min_val:
                pass
            else:
                heapq.heapreplace(self.minheap, v)  # pop且返回堆顶最小值，添加新元素v，调整堆
        else:
            heapq.heappush(self.minheap, v)  # 堆未满，元素直接入堆

    def get_topk(self):
        for v in self.iterable:
            self.push(v)
        return self.minheap


def test_topK():
    import random
    l = list(range(1000))
    random.shuffle(l)

    min_heap = TopK(l, 5).get_topk()
    print(min_heap)
    for _ in range(5):
        print(heapq.heappop(min_heap))


if __name__ == '__main__':
    # head = gen_list(range(10))
    # print_list(head)
    # head = reverseList(head)
    # print_list(head)
    #
    # q = Queue()
    # for i in range(10):
    #     q.append(i)
    # print(q.pop())
    # print(q.pop())
    # print(q.pop())
    # print(q.pop())
    # print(len(q))

    test_topK()