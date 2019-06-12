
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


class QueueWithTwoStacks:
    """
    用两个栈实现队列
    """
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def append(self, x):  # 入队就是往栈1里加
        self._stack1.append(x)

    def pop(self):  # 出队就是从栈2中出
        if self._stack2:  # 如果栈2中还有元素（上次从栈1转移到栈2的元素）则直接从栈2中出
            return self._stack2.pop()
        else:  # 如果栈2是空的，就把栈1的元素全部转移到栈1中
            if self._stack1:
                while self._stack1:
                    self._stack2.append(self._stack1.pop())
                return self._stack2.pop()
            else:
                return None


def test_queue_with_two_stacks():
    q = QueueWithTwoStacks()
    q.append(1)
    q.append(2)
    print(q.pop())
    q.append(3)
    q.append(4)
    print(q.pop())


class StackWithTwoQueues:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def push(self, x):
        if len(self._stack1) == 0:
            self._stack1.append(x)
        elif len(self._stack2) == 0:
            self._stack2.append(x)

        if len(self._stack2) == 1 and len(self._stack1) >= 1:
            while self._stack1:
                self._stack2.append(self._stack1.pop(0))
        elif len(self._stack1) == 1 and len(self._stack2) > 1:
            while self._stack2:
                self._stack1.append(self._stack2.pop(0))

    def pop(self):
        if self._stack1:
            return self._stack1.pop(0)
        elif self._stack2:
            return self._stack2.pop(0)
        else:
            return None


def test_stack_with_two_queues():
    q = StackWithTwoQueues()
    q.push(1)
    q.push(2)
    print(q.pop())
    q.push(3)
    q.push(4)
    print(q.pop())


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

    # test_topK()
    test_queue_with_two_stacks()
    test_stack_with_two_queues()
