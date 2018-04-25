import socket,time

HOST='192.168.1.4'
PORT=9999
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(2)

while 1:
    conn, addr = s.accept()
    while 1:
        print('Connected by', addr)
        data=conn.recv(4096)
        print(data.decode())
        print(time.localtime())
        if not data:
            time.sleep(1)
            break
        conn.sendall(data)
conn.close()