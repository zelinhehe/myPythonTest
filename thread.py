import threading
from time import sleep

shutdown = False


def thread():
    while not shutdown:
        pass


def thread1():
    for i in range(10):
        sleep(1)
        print('-', i)
    print("exit thread1")


def test1():
    t1 = threading.Thread(target=thread1)
    # t1.daemon = True
    t1.setDaemon(True)
    t1.start()
    sleep(1)
    # shutdown = True
    print("t1.join")
    t1.join()
    print("exit main")


def thread_f(arg):
    print(arg)
    sleep(3)
    print('thread_f end.')


def test_daemon():
    t = threading.Thread(target=thread_f, args=('arg', ))
    t.setDaemon(True)
    t.start()
    print('main thread end.')


class ThreadF(threading.Thread):
    def __init__(self, name, arg):
        self.arg = arg
        super().__init__(name=name)

    def run(self):
        print(self.arg)
        sleep(3)
        print('ThreadF end.')


def test_thread_f():
    t = ThreadF('th-1', 'arg')
    t.start()

if __name__ == "__main__":
    # test_daemon()
    test_thread_f()
