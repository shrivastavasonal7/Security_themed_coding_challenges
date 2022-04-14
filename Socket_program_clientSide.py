import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname('localhost')
port = 12345

s.connect((host, port))
msg = s.recv(1024)

s.close()

print(msg.decode('ascii'))