import sys
import os
import socket

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tello

print "Connecting to Tello drone..."

try:
	drone = tello.Tello('192.168.10.2', 8888, False)

	print "Connected to Tello successfully."

	print "Setting the speed to 2 kmpt..."

	drone.set_speed(2)
	
	print "Success."

except socket.error:
	print "Could not connect to Tello drone."