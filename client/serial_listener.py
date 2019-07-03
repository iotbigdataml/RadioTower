###################################################################################################################
# External Dependencies:
#   - python 2.7
#	- time
#	- serial ## pyserial-3.2.1 library
###################################################################################################################

import sys
import time
import serial 
import requests,json

URI = 'http://9ee6a80e.ngrok.io/api/trips/update/bot/arrival'

# Make sure the device/comm port was supplied on the command line. To get a list of valie devices please see
# serialports.py (lists the available ports).

if len(sys.argv) < 2:
    print 'You need to supply the comm port/device on the command line.'
    print 'python serialreader <comm port or device path>'
    exit()
else:
	print
	print '____________________________________________________________'		
	print 'Reading from port ' + sys.argv[1]
	print 'To stop, press control-C'
	print '____________________________________________________________'
	print

# Here we define the serial port. This reflects the settings for the software serial port on the arduino.
# Please refer to the companion arduino code: SoftSerialWrite.ino. Note that no errors are trapped here in the 
# name of brevity. If the comm port/device doesn't exist, it will crash here. For your production code you should
# probably add error handling here (try-catches).

ser = serial.Serial (
    port=sys.argv[1],
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.5, # IMPORTANT, can be lower or higher
    inter_byte_timeout=0.1 # Alternative
)

# Wait a couple of seconds for things to settle (typical in the embedded world ;-)

time.sleep(2)



# This is a pretty simple do-forever loop. If there is anything to read, we read it and print it.
try:
	while True: 
		if ser.in_waiting > 0:				# Check to see if anything is in the buffer					
			line =ser.readline()	
			print(line)
			#print(str(lhttp://fae1f02e.ngrok.ioine[0:10]) == "receiving1")
			#print(len(line))
			#s1="receiving1"
			#print(len(s1))
			if (line[0:10] == "receiving1"):
				j = {'station':'RECV','bot':'11'}
				r =requests.post(URI,data=j)
				#print("check")
			elif (line[0:10] == "receiving2"):
				j = {'station':'RECV','bot':'12'}
				r =requests.post(URI,data=j)
				#print("check")
			elif (line[0:9] == 'shipping1'):
				j = {'station':'SHIP','bot':'11'}
				r =requests.post(URI,data=j)
				#print("check")
			elif (line[0:9] == 'shipping2'):
				j = {'station':'SHIP','bot':'12'}
				r =requests.post(URI,data=j)
				#print("check")
except KeyboardInterrupt:
	print('interrupted')	



