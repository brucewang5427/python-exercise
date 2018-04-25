import socket,time

i=0
HOST='192.168.1.4'
PORT=9999
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
    data=input('please enter: ')
    s.sendall(data.encode())
    data=s.recv(4096)
    print('Received from server: ', repr(data.decode().upper()))
    i += 1
    time.sleep(2)
s.close()
