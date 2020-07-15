from client import Client
from server import Server
import time

client = Client()
server = Server()

print('Exemples using the functions server and client.')
print('What do you want to create?')
choose = input('1: Server /n 2: Client?')

if choose == '1':
    print('Create server...')
elif choose == '2':
    print('Create client...')
else:
    print('Finalizando...')

sleep(3)
