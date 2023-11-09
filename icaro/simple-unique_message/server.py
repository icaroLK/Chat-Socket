import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''Essa é a função primária da biblioteca. 

PRIMEIRO PARÂMETRO ( socket.AF_INET )
    - Especifica o tipo da conexão que vai ser estabelecida, nesse caso conexão de internet
    - Tem vários tipos pra colocar nesse parâmetro -> bluetooth, INET6, etc

SEGUNDO PARÂMETRO ( socket.SOCK_STREAM )  
    - Nesse caso significa que vamos fazer uma conexão TCP
    - Poderia usar o SOCK_DGRAM para uma conexão UDP

'''



# Agora a variável é um socket, mas ainda não tem nenhum lugar especificando pra que esse socket vai ser usado (o socket pode ser usado pra conectar em alguma coisa ou pra hostear alguma coisa)
# Nesse caso a gente quer fazer com que o socket seja um server (hostear alguma coisa), então precisamos deixar isso claro -> Atribuindo um host e uma porta
# Tem como pegar o IP automaticamente pra que o código funcione em diferentes computadores usando o código (não funciona se usar virtual boxes): 
# HOST = socket.gethostbyname(socket.gethostbyname())
HOST = '192.168.0.10'
'''Aqui o HOST vai ser o meu IP
cmd -> ipconfig -> Adaptador Ethernet Ethernet -> IPv4
'''

# Definir a porta a ser usada
PORT = 9999


# Conectar o servidor com o número do HOST e com a porta especificada 
server.bind((HOST, PORT))
'''Aqui precisamos passar os parâmetros em tuplas, por isso os dois parênteses'''


# Agora precisamos fazer com que o servidor fique "ouvindo" requisição de conexões a todo momento
server.listen()
'''Aqui podemos colocar como parâmetro um número para que o servidor se limite a no máximo X conexões'''


while True:
    communication_socket, address = server.accept()

    '''Esse médtodo accept() vai aceitar todas as conexões que aparecerem, caso nao apareça nenhuma ele não faz nada

    Quando a conexão é aceita
        - communication_socket vai representar a conexão com o cliente, ele permite que a gente se conecte e troque informações com o client
        - address vai ser o endereço que essa conexão veio (contém um tupla com o endereõ IP)
    
    A gente não consegue usar a variável "server" pra se conectar direto com o client (ela só serve pra aceitar conexões), então a gente usa o outro socekt chamado communication_socket para fazer de fato a comunicação
    '''
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    '''Precisamos pegar a mensagem enviada pelo client, que está dentro da variavel communication_socekt
    
    O número é o tamanho do buffer então o tamanho (em bytes) 

    Quando a gente envia mensagens via sockets, a gente precisa transformar elas em alguma coisa, a mensagem não pode ir crua (podemos transformar em binário, ou transformar para o código equivalente na tabela ASCII) então quando recebemos precisamos fazer o caminho inverso (decodar) para isso usamos o .decode() e dentro dele passamos a forma de encode que usamos anteriormente
    '''
    print(f"Message from client: {message}")


    # Agora eu quero mandar uma mensagem de confirmação de volta pro cliente que mandou essa mensagem, pra isso preciso usar a variável que a gente deixou para fazer a comunicação ( communication_socket ), porém a gente nao pode mandar a mensagem crua, precisamos encode a mensagem antes (não podemos mandar uma string, precisamos mandar em bytes)
    communication_socket.send(f"Got your message!".encode('utf-8'))


    communication_socket.close()
    '''Aqui o fechamento seria opcional, se voce quiser mandar mais mensagens, pode deixar aberto'''

    print(f"Connection with {address} ended!".decode('utf-8'))
    

