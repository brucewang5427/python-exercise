import socket,sys

host='localhost'
port=9999

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    while 1:
        data = input('Input: ')
        sock.connect((host, port))
        sock.sendall(bytes(data + "\n", 'utf-8'))
        received = str(sock.recv(4096), 'utf-8')
        print("Sent:  {}".format(data))
        print("Received:  {}".format(received))

