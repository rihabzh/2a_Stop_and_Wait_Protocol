import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(1)

print("Waiting for sender...")
conn, addr = s.accept()

while True:
    data = conn.recv(1024).decode()
    print("Frame received:", data)

    ack = "ACK"
    conn.send(ack.encode())
    print("Acknowledgement sent")