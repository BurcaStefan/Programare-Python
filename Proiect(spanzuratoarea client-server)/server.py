import socket

def clients_connection(client1,client2):
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
            client1.send("Conectat la server!\n".encode())
        elif identifier == "client2" and client2 is None:
            client2 = client_socket
            print("Client2 conectat.")
            client2.send("Conectat la server!\n".encode())
    
    return client1, client2
            
def recive_word_and_hint_from_client1(client1):
    word = client1.recv(1024).decode().strip()
    hint = client1.recv(1024).decode().strip()
    return word, hint

def send_word_and_hint_to_client2(client2, word, hint):
    client2.send(word.encode())
    client2.send(hint.encode())
    
if __name__ == '__main__':
    client1=None
    client2=None
    client1, client2= clients_connection(client1,client2)
    word, hint = recive_word_and_hint_from_client1(client1)
    send_word_and_hint_to_client2(client2, word, hint)
