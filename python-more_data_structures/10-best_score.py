#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        sorted_d = sorted(a_dictionary.items(), key=lambda x: x[1])
        return list(dict(sorted_d).keys())[-1]
