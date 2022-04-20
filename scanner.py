#!/bin/python3

import sys
import socket
from datetime import datetime as dt

#Target Define

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate Hostname to IPv4
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 sock.py <ip>")


#Banner

print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(dt.now()))
print("-" * 50)


try:
	for port in range(20,443):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()


except KeyboardInterrupt:
	print("\n Exiting")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()

