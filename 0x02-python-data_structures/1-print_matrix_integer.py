#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if len(matrix[i]) == 0:
            print("".format())
            break
        else:
            for j in range(len(matrix[i])):
                try:
                    matrix[i][j + 1]
                    print("{:d}".format(matrix[i][j]), end=" ")
                except:
                    print("{:d}".format(matrix[i][j]))
    return
