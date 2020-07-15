'''
# Objective: Create a class that can generate a connection using Sockets and
# threading with the objective to receave and send message to each client
# that connect in the server(Including send and receave Jason archives).
# Functions:
# - start_server
# - close_server

# - new_client
# - kill_client
# - send_msg
# - read_msg
# -
'''

import socket
#import threading
#import time
'''
class Server:
    def __init__(self):
'''
print('Work with sockets Client!')

s = socket.socket()
print('Socket Created')
s.bind(('localhost',9999))

s.listen(3)

print('Waiting for connections...')

while True:
    c, addr = s.accept()

    name = c.recv(94).decode()
    print(f'Connect with {name}')

    c.send(bytes('Welcame','utf-8'))

    c.close()
