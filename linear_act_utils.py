import RPi.GPIO as GPIO
import time


def linear_motion_maxspeed(direction, distance):
    # set up GPIO numbering mode
    GPIO.setmode(GPIO.BCM)

    # Define the GPIO pin for the motor controller
    forward_pin = 12
    backward_pin= 16

    GPIO.setup(forward_pin, GPIO.OUT)
    GPIO.setup(backward_pin, GPIO.OUT)

    if direction == "forward": rev_directional_pin = backward_pin
    elif direction == "backward": rev_directional_pin = forward_pin
    else: print(f"ERROR (linear_motion_maxspeed): direction {direction} invalid"); exit(2)
    bias = 1.33
    r_time = (float(distance) / 50) * bias
    print(f"time is: {r_time}")
    GPIO.output(rev_directional_pin, GPIO.LOW)
    time.sleep(r_time)
    GPIO.output(rev_directional_pin, GPIO.HIGH)


def linear_motion_pwm(direction, distance, speed):
    # set up GPIO numbering mode
    GPIO.setmode(GPIO.BCM)