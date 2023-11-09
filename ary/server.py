import socket
import threading
from functions import *

# FUNÇÕES
###############
# SERVER-SIDE #
###############

# ENVIA MENSAGEM PARA TODOS OS PARTICIPANTES DO CHAT
def broadcast(message):
    for client in clients:  
        client.send(message)


# MANTÉM A CONEXÃO DO CLIENTE ATIVA
def session(client):
    while True:
        try:
            message = client.recv(1024) # Tente receber uma mensagem;
            broadcast(message)          # Caso funcione, envie a mensagem para os outros participantes
       
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} saiu do chat.'.encode('ascii'))
            nicknames.remove(nickname)
            break


# CONECTA NOVOS PARTICIPANTES NO CHAT
def new_client():
    while True:
        client, address = server.accept() # ACEITA A ENTRADA DE NOVOS CLIENTES, MOSTRANDO O IP
        print(f'{str(address)} conectado!') # Feedback de conexão

        client.send('NICK'.encode('ascii')) # ENVIA A PALAVRA CHAVE 'NICK' PARA O CLIENTE INFORMAR SEU NICKNAME
        nickname = client.recv(1024).decode('ascii') # RECEBE O NICKNAME DO CLIENTE
        nicknames.append(nickname) # ADICIONA NICKNAME À LISTA
        clients.append(client) # ADICIONA CLIENTE À LISTA

        print(f'Nome: {nickname}')
        broadcast(f'{nickname} entrou no chat.'.encode('ascii')) # AVISA OS OUTROS PARTICIPANTES
        client.send('Conectado.'.encode('ascii')) # AVISA O CLIENTE QUE A CONEXÃO FOI SUCEDIDA

        thread = threading.Thread(target=session, args=(client,)) # Começa a sessão do novo Cliente
        thread.start()


# CÓDIGO

HOST = '127.0.0.1' #localhost - Colocar o IP do Server
PORT = 9999 # Utilizar portas não comuns

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT)) 
server.listen() # Coloca o server em aberto para novas conexões

clients = []
nicknames = []

title('Esperando novos participantes...')
new_client()