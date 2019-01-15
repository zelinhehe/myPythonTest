# @Time    : 2018/7/15 下午4:27


def quick_sort(array):

    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n)


if __name__ == '__main__':

    array = [1, 6, 2, 4, 3, 9, 4, 6, 7, 0]
    print(quick_sort(array))
