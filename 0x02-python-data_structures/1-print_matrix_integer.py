#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        j = 0
        while j < (len(matrix[i]) - 2):
            return print("{:d} {:d} {:d}".format(
                  matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]))
            j += 1

