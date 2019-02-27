import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()

clients = {}


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


# 获取从客户端发送的数据
while True:
    sock, addr = server.accept()
    clients[sock.fileno()] = sock
    # 新建立一个连接socket，就开一个线程去处理
    thread_send = threading.Thread(target=sock_send, args=())
    thread_recv = threading.Thread(target=sock_recv, args=(sock, addr))
    thread_send.start()
    thread_recv.start()
