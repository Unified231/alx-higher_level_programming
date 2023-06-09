"""Print the number of and list of arguments passed to the program."""
import sys

count = len(sys.argv) - 1

if count == 0:
    print("No arguments passed.")
elif count == 1:
    print("One argument passed:", sys.argv[1])
else:
    print("{} arguments passed:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
