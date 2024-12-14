import socket

client1=None
client2=None

def clients_connection():
    global client1, client2
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    
    while client1 is None or client2 is None:
        client_socket, client_address = server_socket.accept()
        identifier = client_socket.recv(1024).decode().strip()
        
        if identifier == "client1" and client1 is None:
            client1 = client_socket
            print("Client1 conectat.")
            client1.send("Conectat la server!\n")
        elif identifier == "client2" and client2 is None:
            client2 = client_socket
            print("Client2 conectat.")
            client2.send("Conectat la server!\n")
    
if __name__ == '__main__':
    clients_connection()