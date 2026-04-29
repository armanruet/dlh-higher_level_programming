#!/usr/bin/python3
def no_c(my_string):
    new_str = []
    for i in my_string:
        if i == "C" or i == "c":
            new_str.append("")
        else:
            new_str.append(i)
    new_new = "".join(new_str)
    return new_new
