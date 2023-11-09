import socket

# Aqui precisamos estabelecer uma conexão com o servidor, então no host precisamos colocar o IP do server

HOST = '192.168.0.10'

# Como eu estou usando o mesmo computador (mesma LAN), eu posso colocar o mesmo IP que está no meu computador, o mesmo IP privado do server. 
# Agora se eu tivesse em um outro computador, o client precisa especificar o host do server 
# Então se eu tiver um outro computador, preciso colocar o mesmo host que está definido no server
# Se estiver em uma rede de internet precisa colocar o IP publico do server (vai na máquina que esta hosteando o server e procura no google myip.is)

# Então no arquivo qu está hosteando (server) você especifica o PRIVATE IP
# E no arquivo que você esta se conectando, voce coloca o PUBLIC address

PORT = 9999

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ja que estamos se conectando e não hosteando, usando a função connect ao invés de listen

socket.connect((HOST, PORT))
'''Isso mandar um request la pro server -> server aceita conexão '''

socket.send("Hello World".encode('utf-8'))
'''Aqui no client a gente se conecta e manda mensagens com o mesmo socket, diferente do servidor, que precisa especificar a comunicação e o endereço que a mensagem chegou'''




print(socket.recv(1024).decode('utf-8'))

