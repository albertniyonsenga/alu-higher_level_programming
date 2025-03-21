#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    return [[element * element for element in indice] for indice in matrix]
