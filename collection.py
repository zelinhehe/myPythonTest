#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/1/15 3:06 PM
# @Author  : Wu Kun
# @Email   : wukun@hlchang.cn
# @File    : deque 
# @Software: PyCharm
# @license : 娱网科道信息技术有限公司 copyright © 2015-2018

import heapq
from collections import deque, OrderedDict


def deque_test():
    q = deque(maxlen=3)
    q.append(1)
    q.extend((2, 3, 4))
    print(q)
    q.appendleft(5)
    print(q)
    q.popleft()
    print(q)


def use_deque():
    def search(lines, pattern, history=5):
        previous_lines = deque(maxlen=history)
        for line in lines:
            if pattern in line:
                yield line, previous_lines
            previous_lines.append(line)

    with open('test.txt') as f:
        for line, prelines in search(f, 'python', 5):
            for pline in prelines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


def heap_test():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    portfolio = [
        {'name': 'IBM', 'shares': '10', 'price': '91.1'},
        {'name': 'APPL', 'shares': '50', 'price': '543.22'},
        {'name': 'FB', 'shares': '200', 'price': '21.09'},
        {'name': 'HPQ', 'shares': '35', 'price': '31.75'},
        {'name': 'YHOO', 'shares': '45', 'price': '6.35'},
        {'name': 'ACME', 'shares': '75', 'price': '115.65'},
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda d: d['price'])
    print(cheap)

    heap = nums[:]
    heapq.heapify(heap)
    print(heap)
    heap.reverse()
    print(heap)
    print(heap.pop())
    print(heapq.heappop(heap))


def priority_queue():

    class PriorityQueue:

        def __init__(self):
            self._queue = []

        def push(self, item, priority):
            heapq.heappush(self._queue, (priority, item))

        def pop(self):
            return heapq.heappop(self._queue)

    q = PriorityQueue()
    q.push('item1', 1)
    q.push('item3', 3)
    q.push('item4', 4)
    q.push('item2', 2)
    q.push('item5', 2)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


def ordered_dict():
    d = OrderedDict()
    d['f'] = 1
    d['b'] = 1
    d['s'] = 1
    d['g'] = 1
    for key, value in d.items():
        print(key, value)


def dict_sort():
    d = {'c': 1, 'd': 4, 'b': 2, 'a': 3}
    d_sort_by_key = sorted(d.items(), key=lambda item: item[0])  # sort by key
    d_sort_by_value = sorted(d.items(), key=lambda item: item[1])  # sort by value
    print(d)
    print(d_sort_by_key)
    print(d_sort_by_value)


if __name__ == '__main__':
    # deque_test()
    # use_deque()
    # heap_test()
    # priority_queue()
    # ordered_dict()
    dict_sort()
