import socket

def main():

    host = socket.gethostbyname('localhost')
    port = 12345
    serversocket = socket.socket()
    serversocket.bind((host, port))
    serversocket.listen(1)
    print("Socket is Listening")

    while True:
        conn,addr = serversocket.accept()
        print("Got connection from %s" % str(addr))
        msg = 'Connection Established' + "\r\n"
        conn.send(msg.encode('ascii'))
        conn.close()


if __name__ == '__main__':
    main()