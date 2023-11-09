import threading
import socket
from functions import *

# FUNÇÕES
###############
# CLIENT-SIDE #
###############

def receive_message():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii')) # ENVIA O NICKNAME AO SERVIDOR COM O GATILHO 'NICK'
            else:
                print(message)
        
        except:
            print('Erro!')
            client.close()
            break


def new_message():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


# CÓDIGO

nickname = input('Digite seu NICKNAME: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

write_thread = threading.Thread(target=new_message)
write_thread.start()