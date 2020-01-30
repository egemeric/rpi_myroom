#!/usr/bin/python3
import socket
import os


while True:
 s = socket.socket()
 s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 port = 12345
 s.bind(('0.0.0.0', port))
 s.listen(5)
 c, addr = s.accept()
 print("success:", addr)
 while True:
    rcvdData = c.recv(5).decode()
    chack=rcvdData

    if(chack[0:3]== "BYE" or chack[0:3]== "bye"): #secret code :D
        os.system('dbus-send --type=method_call --dest=org.gnome.ScreenSaver /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock') #lock gnome 
        response='ok'
        c.send(response.encode())
        c.close()
        break
    else:
        c.close()
        print("closed")
        break

