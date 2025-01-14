#! /usr/bin/python3
# controlled lienar actuator has stroke length of 100mm (3.93 inches)

import argparse
from linear_act_utils import linear_motion_maxspeed, linear_motion_pwm

# ------- Get and Validate User Input -------- #
parser = argparse.ArgumentParser()
parser.add_argument('--direction')
parser.add_argument('--distance')
parser.add_argument('--speed')

args = parser.parse_args()
direction = args.direction
distance = args.distance    # measured in mm

if args.speed != None:  # measured in mm/s; deaults to 50 mm/s
    speed = args.speed
else: speed = 50 

if direction == None or distance == None:   # bad usage case, direction & distance must be provided
    print("Invalid or missing mode; use --direction forward | backward --distance dist_mm"); exit(1)
if float(distance) > 100.0 or float(distance) < 0:    # bad usage case, max stroke length is 100 mm, min is 0 mm
    print("Invalid input for distance. Maximum distance is 100mm"); exit(1)

if float(speed) > 50.0 or float(speed) < 1.0: # bad usage case, max speed is 50 mm/s (design constraint) and min speed is 1 mm/s (artificial constraint)
    print("Invalid input for speed")

# -------------------------------------------- #

#sanity check
print(f"value for direction is {direction}")
print(f"value for distance is {float(distance)}")
print(f"value for speed is {float(speed)}")

# case 1: full speed, no PWM required
linear_motion_maxspeed(direction, distance)