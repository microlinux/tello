import tello
import time

drone = tello.Tello('192.168.10.2', 8888)

drone.takeoff()
time.sleep(5)

drone.set_speed(2)
time.sleep(1)

drone.move_up(3)
time.sleep(5)

drone.move_forward(10)
time.sleep(10)

drone.rotate_cw(180)
time.sleep(5)

drone.move_forward(10)
time.sleep(10)

drone.land()

print 'Flight time: %s' % drone.get_flight_time()
