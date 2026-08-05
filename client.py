import socket

s = socket.socket()
s.connect(("localhost", 8000))

while True:
    reply = input("client: ")
    s.send(reply.encode())
    
    data = s.recv(1024).decode()
    print("MAC Address:", data)