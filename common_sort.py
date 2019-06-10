# @Time    : 2018/7/15 下午4:27

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n)


def quick_sort(array):
    if len(array) < 2:  # 递归结束条件
        return array
    else:
        pivot = array[0]  # 基准元素
        less = [i for i in array[1:] if i <= pivot]  # 比基准元素小的子数组
        greater = [i for i in array[1:] if i > pivot]  # 比基准元素大的子数组
        return quick_sort(less) + [pivot] + quick_sort(greater)  # 合并此次结果


def merge_sorted_list(sorted_i, sorted_j):
    """将两个有序的序列，合并为一个有序的序列"""
    i = j = 0
    new_sorted_list = []

    while i < len(sorted_i) and j < len(sorted_j):
        if sorted_i[i] < sorted_j[j]:
            new_sorted_list.append(sorted_i[i])
            i += 1
        else:
            new_sorted_list.append(sorted_j[j])
            j += 1

    if i < len(sorted_i):
        new_sorted_list.extend(sorted_i[i:])
    else:
        new_sorted_list.extend(sorted_j[j:])
    return new_sorted_list


def test_merge():
    a = [2, 5, 6]
    b = [0, 1, 3, 4, 7, 9]
    print(merge_sorted_list(a, b))


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        middle = len(array)//2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge_sorted_list(left, right)


def heap_sort_by_heapq(iterable):
    from heapq import heappush, heappop, heapify
    # heap = []
    # for i in iterable:
    #     heappush(heap, i)
    heapify(iterable)
    return [heappop(iterable) for i in range(len(iterable))]
    # return [heappop(heap) for i in range(len(heap))]


def binary_search(sorted_array, val):
    if not sorted_array:
        return -1
    begin, end = 0, len(sorted_array) - 1
    while begin <= end:
        middle = (begin + end)//2
        if sorted_array[middle] == val:
            return middle
        elif sorted_array[middle] < val:
            begin = middle + 1
        elif sorted_array[middle] > val:
            end = middle - 1
    return -2


if __name__ == '__main__':

    import random
    l = list(range(10))
    random.shuffle(l)
    print(l)
    print(quick_sort(l))
    print(merge_sort(l))
    # print(heap_sort_by_heapq(l))

    print(binary_search(quick_sort(l), 7))
    import bisect
    r = []
    for i in l:
        bisect.insort(r, i)
    print(r)
