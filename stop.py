#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from adafruit_servokit import ServoKit

# TODO add eggtooth servo
SERVO_TOTAL = 4

pca = ServoKit(channels=16, address=0x40)

def disable_all():
    for i in range(SERVO_TOTAL):
        pca.servo[i].angle = None

def emergency_stop():
    disable_all()
    print("The robot is at rest.")
    
if __name__ == '__main__':
    emergency_stop()
