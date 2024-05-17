#!/usr/bin/env python3
'''
Author: Prince Mikhael Ranjo
Author ID: pranjo
Date Created: 5/17/2024
'''

import sys

# Checks number of arguments
args = len(sys.argv)

# Sets timer to 3 if no arguments are used
if args != 2:
    timer = 3

# Use timer provided by user
else:

    # Have the user add a argument for a countdown timer
    timer = int(sys.argv[1])

# Countdown timer using while loop
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')