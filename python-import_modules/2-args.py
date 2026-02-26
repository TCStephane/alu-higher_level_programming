#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    count = len(arguments)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 arguments:")
        print("1: Hello")
    else:
        print("{} arguments:".format(count))
    for i+1 in range(count):
        print("{}: {}".format(i + 1, arguments[i]))
