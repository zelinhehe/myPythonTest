import time
import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()


class Fetcher:
    def connected(self, key):  # 可写（connect OK）的 callback
        selector.unregister(key.fd)  # 取消注册
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)  # 注册，当client变为可读，则调用readable

    def readable(self, key):  # 可读的 callback
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)  # 取消注册
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()

    def get_url(self, spider_url):
        self.spider_url = spider_url
        url = urlparse(spider_url)
        self.host = url.netloc
        self.data = b""
        self.path = "/" if url.path == "" else url.path
        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)  # 设置为非阻塞
        try:
            self.client.connect((self.host, 80))  # 执行连接，立即返回。不管连接是否完成
        except BlockingIOError as e:
            # 此刻连接还没有完成（应该过会儿就连接完成）注意不是连接失败了，而是还在连接中。
            # 所以可将此连接注册，然后检查是不是连接完成了（EVENT_WRITE）
            pass

        # 注册 如果client变为可写状态，则调用connected方法
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # 事件循环，不停地请求就绪的 socket，并调用对应的回调函数。socket 状态变化以后的回调是由程序员完成的，并不是selector自动完成
    while True:
        ready = selector.select()  # 状态
        for key, mask in ready:
            callback = key.data
            callback(key)

if __name__ == "__main__":
    start_time = time.time()
    for i in range(20):
        Fetcher().get_url("http://shop.projectsedu.com/goods/{}/".format(i))
    loop()
    print(time.time()-start_time)