#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        for row in matrix:
            for element in row:
                element = element * element
                return element
    return matrix
