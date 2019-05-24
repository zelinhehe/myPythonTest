import sys
import time
import socket
import threading


class Client(object):
    def __init__(self, host, port=3333, timeout=1, reconnect=2):
        self.__host = host
        self.__port = port
        self.__timeout = timeout
        self.__buffer_size = 1024
        self.__flag = 1
        self.client = None
        self.__lock = threading.Lock()

    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, new_num):
        self.__flag = new_num

    def __connect(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # client.bind(('0.0.0.0', 12345,))
        client.setblocking(True)
        client.settimeout(self.__timeout)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口复用
        server_host = (self.__host, self.__port)
        try:
            client.connect(server_host)
        except:
            raise
        return client

    def send_msg(self):
        if not self.client:
            return
        while True:
            time.sleep(0.1)
            # data = raw_input()
            data = sys.stdin.readline().strip()
            if "exit" == data.lower():
                with self.__lock:
                    self.flag = 0
                break
            self.client.sendall(data.encode("utf8"))
        return

    def recv_msg(self):
        if not self.client:
            return
        while True:
            with self.__lock:
                if not self.flag:
                    print('ByeBye~~')
                    break
            try:
                data = self.client.recv(self.__buffer_size)
            except socket.timeout:
                continue
            except:
                raise
            if data:
                print("%s\n" % data)
            time.sleep(0.1)
        return

    def run(self):
        self.client = self.__connect()
        send_proc = threading.Thread(target=self.send_msg)
        recv_proc = threading.Thread(target=self.recv_msg)
        recv_proc.start()
        send_proc.start()
        recv_proc.join()
        send_proc.join()
        self.client.close()

if __name__ == "__main__":
    Client('localhost').run()

"""
运行方式：

启动server
python server.py

启动client1
python client.py

启动client2
python client.py

在client1的console中输入任何字符串，client2中立马就可以收到

http://www.imooc.com/article/39675
"""
