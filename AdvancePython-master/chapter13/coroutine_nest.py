# 1. run_until_complete
# import asyncio
# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete()

# 1. loop会被放到future中
# 2. 取消future(task)

import asyncio
import time

async def get_html(sleep_times):
    print("waiting")
    await asyncio.sleep(sleep_times)
    print("done after {}s".format(sleep_times))


def coroutine_run():
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(3)

    tasks = [task1, task2, task3]  # 3个协程

    loop = asyncio.get_event_loop()  # 事件循环
    loop.run_until_complete(asyncio.wait(tasks))


def coroutine_cancel():
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(3)

    tasks = [task1, task2, task3]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:  # ctl + c
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print("cancel task")
            print(task.cancel())
        loop.stop()  #
        loop.run_forever()  # 如果不加此行，取消是会报错：Task was destroyed but it is pending!
    finally:
        loop.close()  #


def chain_coroutine():
    """
    https://docs.python.org/3.6/library/asyncio-task.html#example-chain-coroutines
    """
    async def compute(x, y):
        print("Compute %s + %s ..." % (x, y))
        await asyncio.sleep(1.0)
        return x + y

    async def print_sum(x, y):
        result = await compute(x, y)
        print("%s + %s = %s" % (x, y, result))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()

if __name__ == "__main__":
    # coroutine_run()
    # coroutine_cancel()  # 在命令行运行，并使用ctl + c
    chain_coroutine()


# 注册协程到loop中有两种方法
# 1. 通过ensure_future/create_task
# 2. await
