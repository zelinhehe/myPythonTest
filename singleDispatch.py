import functools


@functools.singledispatch
def f(obj):
    print(obj)


@f.register(str)
def _(text):
    print('text:', text)


@f.register(int)
def _(integer):
    print('integer:', integer)


if __name__ == '__main__':
    f(object)
    f('a')
    f(1)
