#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/11/21 11:05 AM
# @Author  : Wu Kun
# @Email   : wukun@hlchang.cn
# @File    : context 
# @Software: PyCharm
# @license : 娱网科道信息技术有限公司 copyright © 2015-2018

import time


# 自定义写一个上下文管理器
class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'ABCD'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero')
            return True


from contextlib import contextmanager


# 使用内置的装饰器 + 自定义的生成器 => 同样功能的上下文管理器
@contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'ABCD'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


class TakeTime:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(end - self.start)


@contextmanager
def take_time():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(end - start)

if __name__ == '__main__':
    # with TakeTime():
    with take_time():
        for i in range(100):
            pass

    if False:
        print('调用 上下文管理器')
        manager = LookingGlass()
        enter = manager.__enter__()
        print(enter)
        print('12345')
        manager.__exit__(None, None, None)

        print(enter)
        print('12345')

        print('\nwith 上下文管理器')
        with LookingGlass() as enter:
            print(enter)
            print('12345')

        print('\nwith 上下文管理器2')
        with looking_glass() as enter:
            print(enter)
            print('12345')

def f():
    try:
        print('hello')
        return
        print('world')
    finally:
        print('finally')

def f2():
    try:
        print('hello')
        return
        print('world')
    except Exception as e:
        print('exception')
    else:
        print('else')
    finally:
        print('finally')

f2()
