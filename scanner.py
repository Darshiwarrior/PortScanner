#!/bin/python3
import socket
import sys
from datetime import datetime
if len(sys.argv)==2:
	target=socket.gethostbyname(sys.argv[1])
	print(target)
else:
	print("Invalid")
print("-"*50)
print("Scanning the target: "+target)
print("time started: "+str(datetime.now()))
print("-"*50)
try:
	for port in range(50,500):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		
		result=s.connect_ex((target,port))
		if result==0:
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("Exiting Program")
	sys.exit()
except socket.gaierror:
	print("Host Name could not be resolved")
except socket.error:
	print("Could not connect")
	sys.exit()