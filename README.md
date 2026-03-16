# 2a_Stop_and_Wait_Protocol
## AIM 
To write a python program to perform stop and wait protocol
## ALGORITHM
1. Start the program.
2. Get the frame size from the user
3. To create the frame based on the user request.
4. To send frames to server from the client side.
5. If your frames reach the server it will send ACK signal to client
6. Stop the Program
## PROGRAM
# server:
```
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
```
# client:
```
import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    msg = input("Enter frame: ")
    s.send(msg.encode())

    ack = s.recv(1024).decode()
    print("Acknowledgement received:", ack)
```
## OUTPUT
# server:
 [alt text](<Screenshot 2026-03-15 231814.png>)
# client:
[alt text](<Screenshot 2026-03-15 232403.png>)
  
## RESULT
Thus, python program to perform stop and wait protocol was successfully executed.
