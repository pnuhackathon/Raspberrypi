# -*- encoding:utf8 -*-
import os
from socketIO_client import SocketIO, LoggingNamespace
import serial

ser = serial.Serial("/dev/ttyACM0",9600)
ser.flushInput()

def on_response(*args):
    a = args[0]

    print (args[0])
    ser.write(str('c'+args[0]))

def response1(*args):
    print (args[0])
    ser.write(str(args[0]))

    
socket = SocketIO('http://15.164.68.143', 9000, LoggingNamespace)
#socket.emit('connection')
socket.on('Call', on_response)
socket.on('normal', response1)
socket.wait()

