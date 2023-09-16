#the websites responds with how much data there is inside that web page
from distutils import cmd
import socket 
mysock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect('data.pr4e.org',80)
cmd = 'GET http://data.type.org/romemo'
mysock.connect(cmd)
while true:
    data=mysock.srecv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close