import gevent

from gevent import monkey
monkey.patch_all()
from socket import *

def handler(c,addr):
    print("connect from",addr)
    while True:
        data=c.recv(1024).decode()
        if not data:
            break
        print("recv msg:",data)
        c.send(b'recive your message')
    c.close()

HOST='127.0.0.1'
PORT=8888
ADDR=(HOST,PORT)
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

while True:
    c,addr=s.accept()
    gevent.spawn(handler,c,addr)



