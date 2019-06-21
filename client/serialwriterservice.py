from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
import sys
import time
import serial 



# Make sure the device/comm port was supplied on the command line. To get a list of valie devices please see
# serialports.py (lists the available ports).

if len(sys.argv) < 2:
    print('You need to supply the comm port/device on the command line.')
    print('python serialwriter <comm port or device path>')
    exit()
else:
	print('____________________________________________________________')		
	print('Writing to port ' + sys.argv[1])
	print('To stop, press control-C')
	print('____________________________________________________________')

# Here we define the serial port. This reflects the settings for the software serial port on the arduino.
# Please refer to the companion arduino code: SoftSerialRead.ino. Note that no errors are trapped here in the 
# name of brevity. If the comm port/device doesn't exist, it will crash here. For your production code you should
# probably add error handling here (try-catches).

ser = serial.Serial(
    port=sys.argv[1],
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

# Wait a couple of seconds for things to settle (typical in the embedded world ;-)

time.sleep(1)

# This is a pretty simple do-forever loop. We ask the user for some input and we write it out the specified
# port.


app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.debug = True

fulfillmentServiceurl = ""
class Bot1(Resource):
    def get(self):
        message='q+'
        b = str.encode(message)						# Puts the message into bytes
        ser.write(b)								# Writes the bytes to the specified port 
        ser.flush()
        return "Bot 1: Command Issued"
    
    def post(self):
        message='q+'
        b = str.encode(message)						# Puts the message into bytes
        ser.write(b)								# Writes the bytes to the specified port 
        ser.flush()
        return "Bot 1: Command Issued"        

class Bot2(Resource):
    def get(self):
        message='p+'
        b = str.encode(message)						# Puts the message into bytes
        ser.write(b)								# Writes the bytes to the specified port 
        ser.flush()	
        return "Bot 2: Command Issued"
    
    def post(self):      
        message='p+'
        b = str.encode(message)						# Puts the message into bytes
        ser.write(b)								# Writes the bytes to the specified port 
        ser.flush()
        return "Bot 2: Command Issued"

class EnterMaintenance(Resource):
    def get(self):
        message='m+'
        b = str.encode(message)						# Puts the message into bytes
        ser.write(b)								# Writes the bytes to the specified port 
        ser.flush()		
        return "Enter Maintenance: Command Issued"
    
    def post(self):
        message='m+'
        b = str.encode(message)						# Puts the message into bytes
        ser.write(b)								# Writes the bytes to the specified port 
        ser.flush()	
        return "Enter Maintenance: Command Issued"

class ExitMaintenance(Resource):
    def get(self):
        message='n+'
        b = str.encode(message)						# Puts the message into bytes
        ser.write(b)								# Writes the bytes to the specified port 
        ser.flush()		
        return "Exit Maintenance: Command Issued"
    
    def post(self):
        message='n+'
        b = str.encode(message)						# Puts the message into bytes
        ser.write(b)								# Writes the bytes to the specified port 
        ser.flush()	
        return "Exit Maintenance: Command Issued"

api.add_resource(Bot1, '/bot1') # Route_1
api.add_resource(Bot2, '/bot2') # Route_2
api.add_resource(EnterMaintenance, '/entermaintenance') # Route_3
api.add_resource(ExitMaintenance, '/exitmaintenance') # Route_4

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)