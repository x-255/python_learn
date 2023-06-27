import socket

client = socket.socket()

client.connect(('localhost', 3333))

while True:
  msg = input('say:')
  if msg == 'q':
    break
  client.send(msg.encode())
  data=client.recv(1024).decode()
  print(data)

client.close()