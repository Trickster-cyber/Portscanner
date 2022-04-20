#!/usr/bin/pyhton3

import socket,sys,os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Successful")

port = 4444
host = "127.0.0.1"

s.connect((host,port))
print("SUccessful connected")

