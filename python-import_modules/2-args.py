#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Assign the list of arguments (excluding script name) to a variable
    argv = sys.argv[1:]
    count = len(argv)

    # Logic for handling 0, 1, or multiple arguments
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Loop through the list using index to match the requirement
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i]))
