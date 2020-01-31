#!/usr/bin/python3
import socket
import os
PORT_=2020
Listen_="0.0.0.0"
Secret="bye"


while True:
 s = socket.socket()
 s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 port = 12345
 s.bind((Listen_, PORT_))
 s.listen(5)
 c, addr = s.accept()
 print("success:", addr)
 while True:
    rcvdData = c.recv(5).decode()
    chack=rcvdData

    if(chack[0:3]== Secret or chack[0:3]== Secret.lower()): #secret code :D
        os.system('dbus-send --type=method_call --dest=org.gnome.ScreenSaver /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock') #lock gnome 
        response='ok'
        c.send(response.encode())
        c.close()
        break
    else:
        c.close()
        print("closed")
        break

