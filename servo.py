#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/

# Constants
nbPCAServo = 4

# ServoKit object
pca = ServoKit(channels=16, address=0x40)

# Initialize servo min and max impulses
MIN_IMP = [500] * 16
MAX_IMP = [2500] * 16

# Initialize all servos
for i in range(nbPCAServo):
    pca.servo[i].set_pulse_width_range(MIN_IMP[i], MAX_IMP[i])

# Function to move a motor to a specified angle
def move_motor(motor, angle):
    pca.servo[motor].angle = angle
    time.sleep(0.03)  # Adjust the delay as needed

# Walking cycle
def walking_cycle(a = 140, b = 5, c = 5, d = 140):
    LF = 0
    RF = 1
    LR = 2
    RR = 3

    # Stand up from resting position
    move_motor(LF, a - 45)
    move_motor(RF, b + 45) 
    move_motor(LR, c)
    move_motor(RR, d) 

    move_motor(LF, a) 
    move_motor(RF, b) 
    move_motor(LR, c) 
    move_motor(RR, d)  

    for _ in range(12):  # Repeat the cycle 4 times
        move_motor(LF, a - 25)  
        move_motor(LR, c + 15)
        move_motor(LF, a)
        move_motor(LR, c)
        move_motor(RF, b + 25)
        move_motor(RR, d - 15)
        move_motor(RF, b)
        move_motor(RR, d)

# Main function
def main():
    walking_cycle()
    disable_all_motors()

def disable_motor(motor):
    pca.servo[motor].angle = None

def disable_all_motors():
    for i in range(nbPCAServo):
        disable_motor(i)

if __name__ == '__main__':
    main()
