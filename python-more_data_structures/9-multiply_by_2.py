#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key, values in a_dictionary.items():
        new[key] = a_dictionary[key]*2
    return new
