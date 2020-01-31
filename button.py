#! /usr/bin/env python3
import time
import requests
import RPi.GPIO as GPIO
import socket

def get_call(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux python) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/41.0.2227.1 Safari/537.36'}
    response = requests.get(url, headers=headers)
    print("Ok")
def get_lock():
    Port_=2020
    Server_="10.1.1.2"
    s = socket.socket()
    s.connect((Server_,Port_))
    str = "bye"
    s.send(str.encode());
    res=s.recv(5)
    print (res)
    s.close()
Button_Gpio_Pin=12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Button_Gpio_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
URL = "http://10.1.1.10:8080/relay/off.php"
URL2= "http://10.1.1.10:8080/relay/on.php"
while True:  
    if GPIO.input(12) == GPIO.HIGH:
        get_call(URL)
        (URL,URL2)=(URL2,URL) #change the button status
        time.sleep(2)
        if URL2=="http://10.1.1.10:8080/relay/off.php":
           st=1 #statement control(off)
           if  st==1:
               st=0
               if st==0:
                 try:
                    get_lock()
                 except:
                    continue

    time.sleep(0.01)
