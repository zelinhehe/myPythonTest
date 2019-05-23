# gather 和 wait 的区别
# gather 更加high-level，支持分组

import asyncio
import time

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


def test1():
    start_time = time.time()

    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com") for i in range(10)]

    # loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(asyncio.gather(*tasks))

    print(time.time()-start_time)


def test2():
    start_time = time.time()

    loop = asyncio.get_event_loop()
    group1 = [get_html("http://projectsedu.com") for i in range(2)]
    group2 = [get_html("http://www.imooc.com") for i in range(2)]

    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    # group2.cancel()
    loop.run_until_complete(asyncio.gather(group1, group2))

    print(time.time() - start_time)

if __name__ == "__main__":
    # test1()
    test2()
