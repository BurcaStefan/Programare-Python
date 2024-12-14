import socket

def connection_with_server():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    data=client_socket.send("client2".encode())

    data=client_socket.recv(1024).decode()
    print(data)

    return client_socket
    
def recive_word_and_hint_from_server(client_socket):
    word = client_socket.recv(1024).decode().strip()
    hint = client_socket.recv(1024).decode().strip()
    return word, hint    

if __name__ == '__main__':
    client_socket=connection_with_server()
    word, hint = recive_word_and_hint_from_server(client_socket)