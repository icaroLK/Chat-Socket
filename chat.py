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
conn, ender = sock.accept()
print('Conexão em: 'ender)

# loop pra receber um buffer

while True:
    dados = conn.recv(1024) #buffer aceita 1024 bytes (de 1024 em 1024)
    print(dados)
    if not dados:
        print('Fechando conexão')
        conn.close()
        break
    conn.sendall(dados)

