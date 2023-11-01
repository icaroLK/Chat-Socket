import socket

#conectar ao servidor
HOST = '127.0.0.1' #(localhost)
PORT = 9999


sock_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#cliente solicita conexão com o servidor
sock_cliente.connect((HOST, PORT)) #EXIGE QUE SEJA TUPLA

#cliente envia dados para o servidor
sock_cliente.sendall(str.encode('FALA COMIGOOOOO clientao aqui')) #enviamo tudo pro server



dados = sock_cliente.recv(1024)

print('Mensafem recebida do servidor para teste: ')
print(dados.decode())

