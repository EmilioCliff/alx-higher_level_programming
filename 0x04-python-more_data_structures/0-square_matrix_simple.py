#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtx = matrix.copy()
    for row in range(len(new_mtx)):
        new_mtx[row] = list(map(lambda x: x**2, new_mtx[row]))
    return new_mtx
