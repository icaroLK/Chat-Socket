import threading
import socket

# HOST = '127.0.0.1'
HOST = '26.109.78.110'
PORT = 9999


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((HOST, PORT))

server.listen()


'''Vamos definir um Broadcast, Handle method (client connection) and a receive method'''


# Como esse aqui vai ser um room precisamos definir uma lista pros clientes

lista_clientes = []
nicknames = []


def broadcast(msg):
    for client in lista_clientes:
        client.send(msg)
        '''Percorrendo cliente por cliente na lista de clientes e mandando a mensagem pra todos eles'''

    

'''Agora precisamos fazer com que, por exemplo, se o cliente A dizer "oi" precisamos pegar essa mensagem dele e mandar pra todos os clientes, incluindo o A'''


def handle(client):
    while True:
        try:
            msg = client.recv(1024) # tente receber uma mensagem do cliente, e se receber, mande pra todos
            broadcast(msg)
        except:
            # aqui vamos fazer um caso pra que quando der alguma merda ali, pare a conexão com o cliente
            index = lista_clientes.index(client) # Aqui essa função index vai pegar a posição correspondente desse cliente dentro da lista de clientes conectados
            lista_clientes.remove(client) # Aqui tira o client atual da lista de clientes e fecha a conexão com ele
            client.close()
            nickname = nicknames[index] # pega o nickname do client atual
            nicknames.remove(nickname)
            broadcast(f"==={nickname} left the chat!===".encode('ascii'))
            break
    '''Aqui nos estamos abrindo um loop pra constantemente tentar pegar mensagens desse cliente

    Caso esse cliente não esteja la, ele vai entrar no except e o cliente vai "sair da sala"

    Como cada cliente vai ter seu próprio thread, tera uma função dessa rodando pra cada cliente

    '''

# Agora vamos determinar o método pra receber mensagens

def receive():
    while True:
        client, address = server.accept()
        '''Esse server.accept() retorna uma tupla com dois elementos, o primeiro entra na variável server e o segundo entra na variável address
        
        PRIMEIRO ELEMENTO 
            - Objeto em socket
            - Representa a conexão estabelecida com o cliente
            - Permite a troca de dados com o cliente
            - Como é um objeto, ele tem funções e atributos próprios, exemplo desses metodos: send() e recv()

        SEGUNDO ELEMENTO
            - Endereço (IP) do cliente que se conectou
        
        '''
        print(f"Connected with {str(address)}")
        # esse print vai ser só no console do servidor


        #Antes de atribuir o cliente atual a lista de conectados, precisamos pedir pra ele um nickname

        # Pra entrar em contato com o cliente precisamos usar aquele primeiro elemento que veio da função server.accept() - Nele tem diversos métodos incluindo um para enviar mensagens de volta pro cliente, vamos usar ele agora

        client.send('NICK'.encode('ascii'))
        # o cliente vai receber uma mensagem "nick", agora ele vai digitar o nickname que ele quer que seja atribuido a ele, vamos pegar essa resposta dele e atribuir a uma variavel

        nickname = client.recv(1024).decode('ascii')
        # recebendo o nickname escolhido pelo cliente


        nicknames.append(nickname)
        # colocando o nickname escolhido pelo cliente na ultima posição da lista nicknames


        lista_clientes.append(client)
        # colocando o objeto com as informações de contato do cliente na ultima posição da lista de clientes

        print(f"Nickname of the client {address}: {nickname}")

        broadcast(f"{nickname} joined the chat!".encode('ascii'))

        client.send("\n\n(Connected to the server)\n".encode('ascii'))


        '''Ja que precisamos conectar vários clientes ao mesmo tempo, precisamos atribuir uma thread pra cada um deles (pra fazer todas essa funções ao mesmo tempo)'''

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print("Server is listening...")
receive()


