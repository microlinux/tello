Tello Python API
================
DISCLAIMER
----------

I do not own a Tello. This code and documentation is based on the Tello SDK
documentation as of 3/19/2018.

WHAT THE BLEEP IS THIS
----------------------

A Python interface for the Ryze Tello drone.

The tello module provides a Tello class, which interacts with the Tello API.

The Tello has an IP of 192.168.10.1. The device sending commands must be
connected to the Tello WiFi network and have an IP in the 192.168.10.0/24
range.

CREATE A MAGIC TELLO OBJECT
---------------------------

Tello objects require a minimum of 2 parameters to initialize, the local IP
address and port to bind.

Ex. `drone = tello.Tello('192.168.10.2', 8888)`

Methods that require distance or speed parameters expect feet or MPH. Include
parameter imperial=False for meters and KPH.

Ex. `drone = tello.Tello('192.168.10.2', 8888, imperial=False)`

If you send a non-movement command to the Tello and it doesn't respond within .3 seconds, 
or a movement command and it doesn't respond in 5 seconds, a
RuntimeError is raised. You may specify the number of seconds to wait with the
one of two timeout parameters: command\_timeout or move\_timeout.

Ex. `drone = tello.Tello('192.168.10.3', 8888, imperial=False, move_timeout=5, command_timeout=0.5)`

The command\_timeout is used for "simple" commands (set\_speed, get\_speed, get\_battery).
The move\_timeout is used for all "movement" related commands.

When you initialize a Tello object, it attempts to connect to the Tello and
enter command mode. If this fails, a RuntimeError is raised.

DO VARIOUS THINGS
-----------------

Once initialized, a number of methods are available to send commands to the
Tello. It will respond with 'OK', 'FALSE' or a numeric value, which the methods
return.

These methods do what you'd expect. Responses are 'OK' or 'FALSE'.
```python
Tello.takeoff()
Tello.land()
```

Methods that perform vertical or horizontal movements require a single
parameter, distance. Responses are 'OK' or 'FALSE'.

The unit of distance is feet or meters. The SDK accepts distances of 1 to 500
centimeters. Realistically, this translates to .1 - 5 meters or .7 - 16.4 feet.

```python
Tello.move_forward(distance)

Tello.move_backward(distance)

Tello.move_right(distance)

Tello.move_left(distance)

Tello.move_up(distance)

Tello.move_down(distance)
```

Methods that rotate require a single parameter, degrees. The SDK accepts values
from 1 to 360. Responses are 'OK' or 'FALSE'.

```python
Tello.rotate_cw(degrees)

Tello.rotate_ccw(degrees)
```

The method to set speed requires a single parameter, speed. Responses are 'OK'
or 'FALSE'.

The unit of speed is KPH or MPH. The SDK accepts speeds from 1 to 100
centimeters/second. Realistically, this translates to .1 to 3.6 KPH or .1 to 
2.2 MPH.

```python
Tello.set_speed(speed)
```

The method to flip requires a single parameter, direction. The SDK accepts 'l',
'r', 'f', 'b', 'lf', 'lb', 'rf' or 'rb'. Responses are 'OK' or 'FALSE'.

```python
Tello.flip(direction)
```

Methods that retrieve information from the Tello take no parameters. Responses
are numeric values.

Get current speed in KPH or MPH:

```python
Tello.get_speed()
```

Get percent battery life remaining:

```python
Tello.get_battery()
```

Get elapsed flight time in seconds:

```python
Tello.get_flight_time()
```

DO THE HOKEY POKEY
------------------

Put it all together, and you might do something like this.

```python
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
```
