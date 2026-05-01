#!/usr/bin/python3
def weight_average(my_list=[]):
	total = 0
	dev = 0
	for i,j in my_list:
		total += i * j
		dev += j
	return total / dev
