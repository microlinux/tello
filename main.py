import tello
import time

drone = tello.Tello('192.168.10.2', 8888)

drone.takeoff()
time.sleep(10)
drone.land()

print 'Flight time: %s' % drone.get_flight_time()
