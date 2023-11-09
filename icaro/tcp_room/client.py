import socket
import threading


HOST = '127.0.0.1'
PORT = 9999

nickname = input('Choose a nickname: ')


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
'''A partir de agora, o servidor recebeu uma solicitação pra entrar
O servidor vai começar a rodar aquela parte do código onde pede pra colocar o nickname
'''



'''Precisamos definir dois metodos e rodar eles ao mesmo tempo
(pra fazer isso de rodar ao mesmo tempo precisamos usar threads)


METODO 1 (recv)
    - Ficar recebendo mensagens o tempo todo do servidor


METODO 2 (send)
    - Um metodo ouvindo o tempo todo se a gente manda alguma mensagem
'''


def receive():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(msg)
        except:
            print("Ocorreu um erro")
            client.close()
            break

def write():
    while True:
        try:
            msg = f"{nickname}: {input("")}"
            client.send(msg.encode('ascii'))
        except:
            print("Ocorreu um erro")
            client.close()
            break




'''Agora precisamos atribuir um thread pra cara uma dessas funções para que elas possam rodar ao mesmo tempo'''

receive_thread = threading.Thread(target=receive)
receive_thread.start()


write_thread = threading.Thread(target=write)
write_thread.start()