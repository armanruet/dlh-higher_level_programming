#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rows in matrix:
        new_matrix.append([cols**2 for cols in rows])
    return new_matrix
