# python3.3 新加了yield from语法
from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "bobby1": "http://projectsedu.com",
    "bobby2": "http://www.imooc.com",
}

# yield from iterable

# def g1(iterable):
#     yield iterable
#
# def g2(iterable):
#     yield from iterable
#
# for value in g1(range(10)):
#     print(value)
# for value in g2(range(10)):
#     print(value)


def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value

for value in my_chain(my_list, my_dict, range(5, 10)):
    # print(value)
    pass


"""
# main 调用方 g1(委托生成器) gen 子生成器
# yield from会在调用方与子生成器之间建立一个双向通道
"""
def g1():
    r = yield from gen()
    print("g1 recv gen's return:", r)

def gen():
    recv = yield "result1"
    print('gen recv1:', recv)
    recv = yield "result2"
    print('gen recv2:', recv)
    return "return"

def main():
    g = g1()
    r = g.send(None)
    print('main recv1:', r)
    r = g.send("main1")
    print('main recv2:', r)
    try:
        g.send("main2")
    except StopIteration as e:
        pass

main()

