#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

# set up GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the motor controller
forward_pin = 12
backwards_pin= 16

GPIO.setup(forward_pin, GPIO.OUT)
GPIO.setup(backwards_pin, GPIO.OUT)

GPIO.output(backwards_pin, GPIO.LOW)
time.sleep(0.25)
GPIO.output(backwards_pin, GPIO.HIGH)
time.sleep(0.1)

GPIO.output(forward_pin, GPIO.LOW)
time.sleep(0.25)
GPIO.output(forward_pin, GPIO.HIGH)
time.sleep(0.25)

# GPIO.output(forward_pin, GPIO.HIGH)
# GPIO.output(backwards_pin, GPIO.LOW)
# time.sleep(1)
# GPIO.output(forward_pin, GPIO.LOW)

GPIO.cleanup()