#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        for b in i:
            print("{:d}".format(b), end=" ")
        print("")
