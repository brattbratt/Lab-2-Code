import RPi.GPIO as GPIO
from time import sleep

delay=.1
rightout=13
leftout=11
forout=10
backout=12
# Output Pins
rightin=16
leftin=15
forin=18
backin=22
# Input Pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftout,GPIO.OUT)
GPIO.setup(rightout,GPIO.OUT)
GPIO.setup(forout,GPIO.OUT)
GPIO.setup(backout,GPIO.OUT)
# Assign
GPIO.setup(rightin, GPIO.IN, pull_up_down=GPIO.PUD._UP)
GPIO.setup(leftin, GPIO.IN, pull_up_down=GPIO.PUD._UP)
GPIO.setup(forin, GPIO.IN, pull_up_down=GPIO.PUD._UP)
GPIO.setup(backin, GPIO.IN, pull_up_down=GPIO.PUD._UP)
# Assign
try:
    while True:
        forward=GPIO.input(forin)
        back=GPIO.input(backin)
        left=GPIO.input(leftin)
        right=GPIO.input(rightin)
        print("left=",left)
        print("right=",right)

        if forward == 1:
            GPIO.output(forout,1)
        if back == 1:
            GPIO.output(backout,1)
        if left == 1:
            GPIO.output(leftout,1)
        if right == 1:
            GPIO.output(rightout,1)
        
        if forward == 0:
            GPIO.output(forout,0)
        if back == 0:
            GPIO.output(backout,0)
        if left == 0:
            GPIO.output(leftout,0)
        if right == 0:
            GPIO.output(rightout,0)

        sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO ready to go!")
