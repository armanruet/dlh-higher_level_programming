#!/usr/bin/python3
def square_matrix_map(matrix=[]):
	sum = []
	for i in matrix:
		sum.append(list(map(lambda x: x ** 2, i)))
	return sum
