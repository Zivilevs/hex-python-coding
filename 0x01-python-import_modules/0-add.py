#!/usr/bin/python3
# Import a simple function from a simple file


if __name__ == '__main__':
    add = __import__("add_0").add  # needs to be defined
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
