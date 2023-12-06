#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_square = []
    for s in matrix:
        m_square = []
        for i in s:
            m_square.append(i * i)
        new_square.append(m_square)
    return new_square
