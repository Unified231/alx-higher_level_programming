#!/usr/bin/python3
"""Print the sum of all arguments passed to the program."""
import sys

total = 0
for i in range(1, len(sys.argv)):
    total += int(sys.argv[i])
print(total)
