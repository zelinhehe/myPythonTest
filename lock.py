#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/11/20 6:00 PM
# @Author  : Wu Kun
# @Email   : wukun@hlchang.cn
# @File    : lock 
# @Software: PyCharm
# @license : 娱网科道信息技术有限公司 copyright © 2015-2018

import threading
import time

x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        x_lock.acquire()
        print('thread_1: x_lock')
        y_lock.acquire()
        x_lock.release()
        print('thread_1: y_lock')
        y_lock.release()


def thread_2():
    while True:
        y_lock.acquire()
        print('thread_2: y_lock')
        x_lock.acquire()
        y_lock.release()
        print('thread_2: x_lock')
        x_lock.release()


t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()
print('t1')
t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()
print('t2')

print('end')

time.sleep(100)

