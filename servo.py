#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
import random
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/

# Constants
nbPCAServo = 4
LF = 0
RF = 1
LR = 2
RR = 3
TOOTH = 4

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

# Stand up from resting
def stand(a = 140, b = 5, c = 5, d = 140):
    move_motor(LF, a - 45)
    move_motor(RF, b + 45)
    move_motor(LR, c)
    move_motor(RR, d)

    move_motor(LF, a)
    move_motor(RF, b)
    move_motor(LR, c)
    move_motor(RR, d)

# Lay down and rest
def lay_down():
    move_motor(LF, 90)
    move_motor(RF, 55)
    move_motor(LR, 55)
    move_motor(RR, 90)

# Walking cycle
def walking_cycle(a = 140, b = 5, c = 5, d = 140):

    # Stand up from resting position


    for _ in range(12):  # Repeat the cycle 4 times
        move_motor(LF, a - 25)
        display()
        move_motor(RR, d + 5) #new
        display()
        move_motor(LR, c + 15)
        display()
        move_motor(LF, a)
        display()
        move_motor(LR, c)
        display()
        move_motor(RF, b + 25)
        display()
        move_motor(LR, c - 5)
        display()
        move_motor(RR, d - 15)
        display()
        move_motor(RF, b)
        display()
        move_motor(RR, d)
        display()

# Main function
def main():
    lay_down()
    time.sleep(1)
    walking_cycle()
    time.sleep(1)
    lay_down()
    time.sleep(1)
    stop()

def disable_motor(motor):
    pca.servo[motor].angle = None

def display():
    move_motor(4, 90)
    for _ in range(1):
        move_motor(4, random.randint(0, 140))

# Disable all motors
def stop():
    for i in range(nbPCAServo):
        disable_motor(i)

if __name__ == '__main__':
    main()
