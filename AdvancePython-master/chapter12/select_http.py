# 1. epoll并不代表一定比select好
# 在并发高的情况下，连接活跃度不是很高， epoll比select
# 并发性不高，同时连接很活跃， select比epoll好

# selector封装了select，并提供了注册机制。select本身是不支持register模式

"""
使用 select 完成 http请求
    select + 注册回调 + 事件循环
    并发性高
    使用单线程
"""

import time
import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
urls = []
stop = False


class Fetcher:
    def __init__(self):
        self.client = None
        self.host = ""
        self.path = ""
        self.spider_url = ""
        self.data = ""

    def connected(self, key):
        """ 可写（connect OK）的 callback"""
        selector.unregister(key.fd)  # 取消注册
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)  # 注册，当client变为可读，则调用readable

    def readable(self, key):
        """ 可读的 callback"""
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)  # 取消注册
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, spider_url):
        self.spider_url = spider_url
        url = urlparse(spider_url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)  # 设置为非阻塞
        try:
            self.client.connect((self.host, 80))  # 执行连接，立即返回。不管连接是否完成
        except BlockingIOError as e:
            # 此刻连接还没有完成（应该过会儿就连接完成）注意不是连接失败了，而是还在连接中。
            # 所以可将此连接注册，然后检查是不是连接完成了（EVENT_WRITE）
            pass  # [Errno 36] Operation now in progress

        # 注册 如果client变为可写状态，则调用connected方法
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    """
    事件循环，不停地请求就绪的 socket，并调用对应的回调函数
    socket 状态变化以后的回调是由程序员完成的，并不是selector自动完成
    """
    while not stop:
        ready = selector.select()  # 状态
        for key, mask in ready:
            print("fd:{} events:{} callback: {}".format(key.fd, key.events, key.data))
            callback = key.data
            callback(key)
    # 回调+事件循环+select(poll/epoll)

if __name__ == "__main__":
    # fetcher = Fetcher()
    start_time = time.time()

    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)

    loop()

    print(time.time()-start_time)

# def get_url(url):
#     #通过socket请求html
#     url = urlparse(url)
#     host = url.netloc
#     path = url.path
#     if path == "":
#         path = "/"
# 
#     #建立socket连接
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.setblocking(False)
#     try:
#         client.connect((host, 80)) #阻塞不会消耗cpu
#     except BlockingIOError as e:
#         pass
# 
#     #不停的询问连接是否建立好， 需要while循环不停的去检查状态
#     #做计算任务或者再次发起其他的连接请求
# 
#     while True:
#         try:
#             client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
#             break
#         except OSError as e:
#             pass
# 
# 
#     data = b""
#     while True:
#         try:
#             d = client.recv(1024)
#         except BlockingIOError as e:
#             continue
#         if d:
#             data += d
#         else:
#             break
# 
#     data = data.decode("utf8")
#     html_data = data.split("\r\n\r\n")[1]
#     print(html_data)
#     client.close()




