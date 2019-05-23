import asyncio


def call_soon_test():
    def callback(sleep_times):
        print("sleep {} success".format(sleep_times))

    def stoploop(loop):
        loop.stop()

    loop = asyncio.get_event_loop()
    loop.call_soon(callback, 2)
    loop.call_soon(stoploop, loop)
    loop.run_forever()


def call_later_test():
    def callback(sleep_times):
        print("sleep {} success".format(sleep_times))

    def stoploop(loop):
        loop.stop()

    loop = asyncio.get_event_loop()
    loop.call_later(2, callback, 2)  # def call_later(self, delay, callback, *args):
    loop.call_later(1, callback, 1)
    loop.call_later(3, callback, 3)
    loop.call_later(0, callback, 0)
    loop.call_soon(callback, 4)
    # loop.call_soon(stoploop, loop)
    loop.run_forever()


def call_at_test():
    def callback(sleep_times, loop):
        print("success time {}".format(loop.time()))

    def stoploop(loop):
        loop.stop()

    loop = asyncio.get_event_loop()
    now = loop.time()
    loop.call_at(now+2, callback, 2, loop)
    loop.call_at(now+1, callback, 1, loop)
    loop.call_at(now+3, callback, 3, loop)
    # loop.call_soon(stoploop, loop)
    loop.call_soon(callback, 4, loop)
    loop.run_forever()


if __name__ == "__main__":
    # call_soon_test()
    # call_later_test()
    call_at_test()
