from datetime import datetime
import socket
import threading
client = socket.socket()
username = input("Username: ").strip()
client.connect(("localhost", 12345))
client.send(username.encode())
def recieve():
    while True:
        print(client.recv(1024).decode())


thread = threading.Thread(target=recieve, daemon=True).start()
print("Send messages via typing below: ")
while True:
    message = input()
    now = datetime.now()
    message = f'[{now}] ' + username + ": " + message
    client.send(message.encode())