import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 6666))

def sender(msg):
    s.send(bytes(msg, "utf-8"))

def reciver():
    msg=s.recv(2048).decode('utf-8')
