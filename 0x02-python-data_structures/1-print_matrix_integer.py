#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        j = 0
        while j < (len(matrix[i]) - 2):
            print("{:d} {:d} {:d}$".format(
                  matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]))
            j += 1
            i = 0
    while i < (len(matrix[0]) - 1):
        print('-', end="")
        i += 1
    else:
        print('$')
    return ('$')
