#!/usr/bin/env python3
'''
Author: Prince Mikhael Ranjo
Author ID: pranjo
Date Created: 5/17/2024
'''

import sys

# Have the user add a argument for a countdown timer
timer = int(sys.argv[1])

# Countdown timer using while loop
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')