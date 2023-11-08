import socket

# PRECISAMOS NOS CONECTAR NO SERVIDOR
HOST = '127.0.0.1'
PORT = 9999

sock_cliente = socket.scoket(socket.AF_INET, socket.SOCK_STREAM)

# CLIENTE SOLICITA CONEXÃO COM O SERVIDOR
sock_cliente.connect((HOST, PORT))

# CLIENTE ENVIA DADOS PARA O SERVIDOR
sock_cliente.sendall(str.encode('fala c a clientadas aqui'))

dados = sock_cliente.recv(1024)
print('Mensagem recebida do servidor para teste: ')
print(dados.decode())
