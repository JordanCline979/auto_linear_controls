#! /usr/bin/python3

from linear_act_utils import linear_motion_maxspeed
import time

linear_motion_maxspeed("forward", 5)
time.sleep(0.01)
linear_motion_maxspeed("backward", 5)
