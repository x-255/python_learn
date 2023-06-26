import socket

server = socket.socket()

server.bind(('localhost', 3333))  # 绑定要监听的端口

server.listen(1)  # 监听

conn, address = server.accept()  # 等待连接

while True:
    data = conn.recv(1024).decode()
    print(f'req={data}')

    msg = input('res:')
    if msg == 'q':
        break
    conn.send(msg.encode())

conn.close()
server.close()
