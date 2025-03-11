#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if not i:
            print("")
        for innum in i:
            if innum == i[-1]:
                print("{:d}".format(innum))
            else:
                print("{:d}".format(innum), end="")
