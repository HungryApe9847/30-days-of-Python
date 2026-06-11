import socket
import threading

clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()
def broadcast(message):
    for client in clients:
        client.send(message.encode())
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            print(message.decode())
            broadcast(message.decode())
        except:
            clients.remove(client)
            client.close()
            break
def accept_clients():
    while True:
        client, address = server.accept()
        username = client.recv(1024).decode()
        print("Connected: ", username)
        broadcast(f"{username} connected!")
        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,), daemon=True)
        thread.start()
print("server running...")
accept_clients()