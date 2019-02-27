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

if __name__ == "__main__":
    t1 = threading.Thread(target=thread1)
    # t1.daemon = True
    t1.start()
    sleep(1)
    # shutdown = True
    print("t1.join")
    t1.join()
    print("exit main")
