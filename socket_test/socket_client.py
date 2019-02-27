import socket
import threading


def sock_send(sock):
    print(dir(sock))
    while True:
        re_data = input()
        if re_data == 'exit':
            sock.close()
            return
        sock.send(re_data.encode("utf8"))


def sock_recv(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            sock.close()
            return
        print(data.decode("utf8"))


sock_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_client.connect(('127.0.0.1', 8000))

thread_send = threading.Thread(target=sock_send, args=(sock_client, ))
thread_recv = threading.Thread(target=sock_recv, args=(sock_client, ))
thread_send.start()
thread_recv.start()
