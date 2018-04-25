import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('connection from: '.format(self.client_address[0]))
        if self.request.recv(1024)=='auth':
            print('auth')
            while 1:
                self.request.send('Username: ')
                username=self.request.recv(1024).strip()
                if username=='chenggang':
                    self.request.send('welcome {0}, you are authenticated'.format(username))
                    print('Correct! Welcome!')
                    break
                else:
                    self.request.send('sorry you are not authenciated')
                    continue


if __name__=='__main__':
    host='localhost'
    port=9999
    server=socketserver.ThreadingTCPServer((host,port),MyTCPHandler)
    server.serve_forever()