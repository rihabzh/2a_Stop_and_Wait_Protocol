import socket

s = socket.socket()
s.bind(("localhost", 8000))
s.listen(1)
print("server is listening")

tables = {
    "192.168.1.1": "AA:BB:CC:DD",
    "192.168.1.2": "AA:CC:BB:DD",
    "192.168.1.3": "AA:DD:CC:BB"
}

c, ad = s.accept()
print("server is connected",ad)

while True:
    data = c.recv(1024).decode()
    
    if data in tables:
        c.send(tables[data].encode())
    else:
        c.send("MAC not found".encode())