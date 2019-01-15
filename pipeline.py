# @Time    : 2018/9/14 下午4:49
# @Author  : WuKun
# @Email   : wukun@hlchang.cn

from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even_filter(nums):
    return filter(lambda x: x % 2 == 0, nums)


def multiply_by_three(nums):
    return map(lambda x: x*3, nums)


def convert_to_string(nums):
    return map(lambda x: 'The Number: %s' % x,  nums)


def pipeline_func(data, fns):

    return reduce(lambda a, x: x(a),   fns,   data)


def pipeline_run():
    # 1
    pipeline = convert_to_string(multiply_by_three(even_filter(nums)))
    for num in pipeline:
        print(num)

    # 2
    def pipeline_func(data, fns):
        def f(a, x):
            print(a, x)
            return x(a)
        return reduce(f, fns, data)
        # return reduce(lambda a, x: x(a), fns, data)

    result = pipeline_func(nums, [even_filter, multiply_by_three, convert_to_string])
    for i in result:
        print(i)

    def f(x, y):
        print(x, y)
        return x + y
    print(reduce(f, [1, 2, 3, 4, 5]))
    print('\n')
    print(reduce(f, [1, 2, 3, 4, 5], 6))


"""
-----------------------------------------------
"""


class Pipe(object):
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        def generator():
            for obj in other:
                if obj is not None:
                    yield self.func(obj)
        return generator()


@Pipe
def even_filter1(num):
    return num if num % 2 == 0 else None


@Pipe
def multiply_by_three1(num):
    return num*3


@Pipe
def convert_to_string1(num):
    return 'The Number: %s' % num


@Pipe
def echo(item):
    print(item)
    return item


def force(sqs):
    print(sqs)
    for item in sqs:
        # print(item)
        pass


def pipeline1_run():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    force(nums | even_filter1 | multiply_by_three1 | convert_to_string1 | echo)


if __name__ == '__main__':
    pipeline_run()
    pipeline1_run()
