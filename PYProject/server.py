import socket

# CRIANDO DO SOCKET E INFO
HOST = "127.0.0.1"
PORT = 9999


### IPV4 É O PARÂMETRO AF_INET
# TCP É O PARÂMETRO SOCK_STREAM


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#PLUG DO IP COM A FUNÇÃO BIND


sock.bind((HOST, PORT)) # EXIGE QUE SEJA TUPLA

# 127.0.0.1:9999
sock.listen()


print(f'O servidor {HOST}:{PORT} está ativo aguardando conexões')

# função que é acessa pelo connect do cliente, retorna 2 parametros

# conn é o socket do cliente e ender e o endereço

# aqui é o ponto onde conectamos um clinete

# para termos varios clientes precisamos de uma loop infinito ($toDO00)
while True: 
    try: 
        conn, ender = sock.accept()
        # ender[0] = IP ender[1] = PORTA
        nome = conn.recv(50).decode() #receber dados em utf-8
        print(f"Conexão em sucesso com o cliente: {nome} - {ender[0]}:{ender[1]}")
    except:
        print("algum erro de conexão ocorreu... tente novamente")
        continue

# loop pra receber dados

    while True:
        try: 
            mensagem = conn.recv(1024).decode() #buffer aceita 1024 bytes (de 1024 em 1024)
            mensagemNome = nome + " >> " + mensagem 
            print(mensagemNome)
        except: 
            print("ocorreu um erro")
            conn.close()
        break 
      



