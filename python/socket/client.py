import socket
'''
class Client:
    def __init__(self):
        print('Work with sockets Client!')
'''

HOST = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall((b'Hello,word'))
    data = s.recv(1024)

print('received', repr(data))
