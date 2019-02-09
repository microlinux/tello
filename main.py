import sys
import termios
import contextlib
import tello
import time


@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


def main():
    drone = tello.Tello('192.168.10.2', 8888)
    print 'exit with ^C or ^D'
    with raw_mode(sys.stdin):
        try:
            while True:
                ch = sys.stdin.read(1)
                if not ch or ch == chr(4):
                    break

                if ch == 'z':
                	drone.takeoff()

                if ch == 'x':
                	drone.land()

                if ch == 'd':
                	drone.rotate_cw(30)

                if ch == 'a':
                	drone.rotate_acw(30)

                if ch == 'c':
                	Tello.get_battery()
                	
        except (KeyboardInterrupt, EOFError):
            pass


if __name__ == '__main__':
    main()