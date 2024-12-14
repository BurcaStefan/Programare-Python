import socket

def connection_with_server():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    data=client_socket.send("client2".encode())

    data=client_socket.recv(1024).decode()
    print(data)

    client_socket.close()
    
if __name__ == '__main__':
    connection_with_server()