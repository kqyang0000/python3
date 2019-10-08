import socket
import threading
import time

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP及端口
s.bind(('127.0.0.1', 9999))
# 监听端口
s.listen(5)


def tcplink(sock, addr):
    print("Accept a new connection from %s:%s..." % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)


while True:
    # 接收一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理请求
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
