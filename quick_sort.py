# @Time    : 2018/7/15 下午4:27

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n)


def quick_sort(array):

    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


def test_quick_sort():
    import random
    l = list(range(10))
    random.shuffle(l)
    print(l)
    print(quick_sort(l))


def merge_sorted_list(sorted_i, sorted_j):
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

if __name__ == '__main__':

    test_quick_sort()
    test_merge()
