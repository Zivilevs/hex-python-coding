#!/usr/bin/python3
import sys

# print number of arguments


def length():
    number = len(sys.argv)
    arg = number - 1

    print("{} {}:".format(arg, "argument" if arg == 0 else "arguments"))
    for i in range(1, number):
        print("{}: {}".format(i, sys.argv[i]))

if __name__ == '__main__':
    length()
