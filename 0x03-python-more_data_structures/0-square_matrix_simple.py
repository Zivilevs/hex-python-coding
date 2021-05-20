#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    length = len(matrix[0])
    new_matrix = []
    new_row = []
    for row in matrix:
        new_row = []
        for i in range(length):
            x = row[i] ** 2
            new_row.append(x)
        new_matrix.append(new_row)
    return new_matrix

'''
# with map, lambda, walrus
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = list(map((lambda x: x ** 2),[x := row[i] for i in
                            range(len(matrix[0]))]))
        new_matrix.append(new_row)
    return new_matrix
'''
