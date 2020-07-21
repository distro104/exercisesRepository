'''
# Objective: Create a class that can generate a connection using Sockets and
# threading with the objective to receave and send message to each client
# that connect in the server(Including send and receave Jason archives).
# Functions:
# - new_conn
# - kill_conn
# - send_msg
# - read_msg
# -
'''
import socket
#import threading
import time

'''
class Server:
    def __init__(self):
        self.s = None
        self.host = socket.gethostname()
        self.door = 1234
        self.conn = None
        self.addr = None
        self.data = None


    def start_server(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind((socket.gethostname(),1234))
        self.s.listen(3)
        print('Waiting connections...')

        self.conn, self.addr = self.s.accept()
        print(f'Connected with {self.addr}')
        self.conn.send(bytes('Welcame to the jungle!!!','utf-8'))

        while True:
            self.data = self.s.recv(100)
            if len(self.data) == 0:
                print(f'Value in coon: {self.conn}')
                print(f'value in addr: {self.addr}')
                print('Finishing connection')
                self.s.close()
                break
            else:
                self.conn.send(bytes('Msg receaved BRO!','utf-8'))
'''


HOST = '127.0.0.1'
PORT = 1234
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn , addr = s.accept()
        with conn:
            print(f'Connected by:{addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
