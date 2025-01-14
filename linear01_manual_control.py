#! /usr/bin/python3
# controlled lienar actuator has stroke length of 100mm (3.93 inches)

import argparse
from time import sleep

# ------- Get and Validate User Input -------- #
parser = argparse.ArgumentParser()
parser.add_argument('--direction')
parser.add_argument('--distance')