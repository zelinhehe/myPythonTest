#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/9/18 下午4:22
# @Author  : WuKun
# @Email   : wukun@hlchang.cn
# @File    : decorator_class 
# @Software: PyCharm
# @license : 娱网科道信息技术有限公司 copyright © 2015-2018


class myDec(object):

    def __init__(self, fn):
        print('inside myDec.__init__()')
        self.fn = fn

    def __call__(self, *args, **kwargs):
        self.fn()
        print('inside myDec.__call__()')


@myDec
def func():
    print('inside func()')


print('finished decorating func()')

# func()


def proxy(func):
    def warp():
        print('START log')
        result = func()
        print('END log')
        return result
    return warp


@proxy
def say_hello():
    print('hello')


if __name__ == '__main__':
    say_hello()
    say_hello = proxy(say_hello)
    say_hello()
