#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        c = a / b
        print("{:d} / {:d} = {}".format(a, b, c))

    except ZeroDivisionError:
        c = None
    finally:
        print("Inside result: {}".format(c))
    return c
