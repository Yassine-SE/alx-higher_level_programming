#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        lst_len = len(i)
        for b in range(lst_len):
            if b == (lst_len - 1):
                print("{:d}".format(i[b]), end="")
            else:
                print("{:d}".format(i[b]), end=" ")
        print("")
