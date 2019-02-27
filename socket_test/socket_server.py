import socket
import threading

"""
服务端：
    支持多个客户端同时连接
    输入 0 ，显示所有已连接客户端，每行代表一个客户端连接，开头的数字是此客户端连接的fd
    向指定客户端发送消息：先输入客户端的fd，后面加发送内容
"""


def sock_recv(sock, addr):
    print(str(addr))
    while True:
        data = sock.recv(1024)  # 一次获取1k的数据
        if not data:
            sock.close()
            return
        print(str(addr) + ': ', data.decode("utf8"))


def sock_send():
    while True:
        data = input()
        if data == '0':
            for fd, client in clients.items():
                print(fd, str(client))
            continue
        else:
            i = data[0]
            sock = clients[int(i)]
            sock.send(data[1:].encode("utf8"))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()

clients = {}  # save socket accepted. key is fd(fileno), value is socket object.

# 获取从客户端发送的数据
while True:
    sock, addr = server.accept()

    clients[sock.fileno()] = sock

    # 新建立一个连接socket，就开一个线程去处理
    thread_send = threading.Thread(target=sock_send, args=())
    thread_recv = threading.Thread(target=sock_recv, args=(sock, addr))
    thread_send.start()
    thread_recv.start()
