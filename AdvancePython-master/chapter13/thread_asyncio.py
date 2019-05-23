""" 使用多线程：在协程中集成阻塞io
    协程是单线程模式
    asyncio 是解决异步io编程的解决方案。异步IO包括 多线程、多进程、协程
    我们知道，协程里不能加入阻塞io。但是有些接口或库只有阻塞形式的，此时我们就把阻塞io放到线程中。
    每个线程池executor，作为一个异步任务task

    方法 get_url 是阻塞的（connect）
"""

import asyncio
import socket
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse


def get_url(origin_url):
    # 通过socket请求html
    url = urlparse(origin_url)
    host = url.netloc
    path = "/" if url.path == "" else url.path

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == "__main__":
    import time
    start_time = time.time()

    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(10)
    tasks = []
    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        task = loop.run_in_executor(executor, get_url, url)
        # task = get_url(url)
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))

    print("last time:{}".format(time.time()-start_time))

# 每个线程池executor，作为一个异步任务task
