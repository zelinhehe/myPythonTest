# 获取协程的返回值
import asyncio
from functools import partial

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "bobby"


def callback(url, future):
    print(url)
    print("send email to bobby")
    print(future)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()  # 事件循环，可以往里面注册协程
    # future = asyncio.ensure_future(get_html("http://www.imooc.com"))  # 将协程注册到loop中
    task = loop.create_task(get_html("http://www.imooc.com"))  # 将协程注册到loop中
    task.add_done_callback(partial(callback, "http://www.imooc.com"))
    # loop.run_until_complete(future)
    loop.run_until_complete(task)

    print(task.result())
