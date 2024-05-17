#!/usr/bin/env python3

import sys

# Checks the number of arguments(calling the file counts as 1 argument)
args = len(sys.argv)

# Prints a usage message if there are less or more than 2 arguments(check for 3 as calling the file by "./lab2d.py" counts as 1 argument)
if args != 3:
    print('Usage: ./lab2d.py name age')
    sys.exit()

# Create Variables that store arguments
# ***arguments are stored as string objects***
name = sys.argv[1]
age = sys.argv[2]

# Prints out text
print('Hi ' + name + ', you are ' + age + ' years old.')