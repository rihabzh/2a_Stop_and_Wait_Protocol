import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    msg = input("Enter frame: ")
    s.send(msg.encode())

    ack = s.recv(1024).decode()
    print("Acknowledgement received:", ack)