# asyncio 没有提供http协议的接口 aiohttp
import time
import asyncio
import socket
from urllib.parse import urlparse


async def get_url(origin_url):
    # 请求html
    url = urlparse(origin_url)
    host = url.netloc
    path = "/" if url.path == "" else url.path

    # 建立连接
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode("utf8")
        all_lines.append(data)
    html = "\n".join(all_lines)
    return html

async def main():
    tasks = []
    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        tasks.append(asyncio.ensure_future(get_url(url)))

    for task in asyncio.as_completed(tasks):  # 完成一个task就获取结果，而不是等所有的task都完成
        result = await task
        print(result)

if __name__ == "__main__":
    start_time = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    print('last time:{}'.format(time.time()-start_time))



