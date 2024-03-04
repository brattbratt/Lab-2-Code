import RPi.GPIO as GPIO
from time import sleep

# Define Input Pins
leftin = 15
rightin = 16
forin = 18
backin = 22
# Define Output Pins
rightout = 13
leftout = 11
forout = 10
backout = 12

# Board Pin Mapping
GPIO.setmode(GPIO.BOARD)
# Outputs
[GPIO.setup(pin, GPIO.OUT) for pin in [leftout, rightout, forout, backout]]
# Inputs
[GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_UP) for pin in [rightin, leftin, forin, backin]]

# Classes To Define States
class StateMachine:
    def __init__(self):
        self.current_state = 'stop'

    def stop(self):
        self.current_state = 'stop'
        GPIO.output(forout,0)
        GPIO.output(backout,0)
        GPIO.output(leftout,0)
        GPIO.output(rightout,0)
    
    def forward(self):
        self.current_state = 'forward'
        GPIO.output(forout,1)
        GPIO.output(backout,0)
        GPIO.output(leftout,0)
        GPIO.output(rightout,0)
    
    def back(self):
        self.current_state = 'back'
        GPIO.output(forout,0)
        GPIO.output(backout,1)
        GPIO.output(leftout,0)
        GPIO.output(rightout,0)

    def left(self):
        self.current_state = 'left'
        GPIO.output(forout,0)
        GPIO.output(backout,0)
        GPIO.output(leftout,1)
        GPIO.output(rightout,0)
    
    def right(self):
        self.current_state = 'right'
        GPIO.output(forout,0)
        GPIO.output(backout,0)
        GPIO.output(leftout,0)
        GPIO.output(rightout,1)

# Callback Function To Change States
def pin_callback(channel):
    global machine
    if channel == forward:
        machine.foward()
        print(machine.current_state)
    elif channel == back:
        machine.back()
        print(machine.current_state)
    elif channel == left:
        machine.left()
        print(machine.current_state)
    elif channel == right:
        machine.right()
        print(machine.current_state)
    else:
        machine.stop()
        print(machine.current_state)

# Create State Machine Instance
machine = StateMachine()

# Event Detection
GPIO.add_event_detection(forin, GPIO.RISING, callback=pin_callback)
GPIO.add_event_detection(backin, GPIO.RISING, callback=pin_callback)
GPIO.add_event_detection(leftin, GPIO.RISING, callback=pin_callback)
GPIO.add_event_detection(rightin, GPIO.RISING, callback=pin_callback)

try:
    while True:
        forward = GPIO.input(forin)
        back = GPIO.input(backin)
        left = GPIO.input(leftin)
        right = GPIO.input(rightin)
        sleep(0.1) # 100ms delay to avoid overflow

except KeyboardInterrupt:
    machine.stop()
    GPIO.cleanup()
    print("GPIO Ready to Go!")


