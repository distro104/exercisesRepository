import socket
'''
class Client:
    def __init__(self):
        print('Work with sockets Client!')
'''
c = socket.socket()

c.connect(('localhost',9999))

name = input('Enter Your name:')
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())
