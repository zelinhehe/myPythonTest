import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)  # 一次获取1k的数据
        print(data.decode("utf8"))
        re_data = input()
        sock.send(re_data.encode("utf8"))


# 获取从客户端发送的数据
while True:
    sock, addr = server.accept()

    # 新建立一个连接socket，就开一个线程去处理
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    # data = sock.recv(1024)
    # print(data.decode("utf8"))
    # re_data = input()
    # sock.send(re_data.encode("utf8"))
    # server.close()
    # sock.close()
