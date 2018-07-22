import socket
import threading
import time
import traceback
import webbrowser
import string
import speech_recognition as sr
import tello

# connect to Tello
drone = tello.Tello('192.168.10.3', 8888)

# obtain audio 
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print ( "Speak to the computer what commands you want your tello drone to do" )
        audio = r.listen(source)

    if "speed" in r.recognize_google(audio):
        # Make a drone command to obtain speed
        print ( drone.get_speed() )

    if "battery" in r.recognize_google(audio):
        # Make a drone command to obtain battery
        print ( drone.get_battery() )