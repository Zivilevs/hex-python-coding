#!/usr/bin/python3
# this def is used in the program and on the CLI


def add(a, b):
    return(a + b)

a = 1       # a, b must be before name == main,
b = 2       # if they are used in program later.

if __name__ == 'add_0':
    add(a, b)
# '__main__' is name of this file, but in in this case
# it is wanted to be specific.
print("{} + {} = {}".format(a, b, add(a, b)))
