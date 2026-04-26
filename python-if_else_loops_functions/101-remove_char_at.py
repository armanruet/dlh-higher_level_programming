#!/usr/bin/python3
def remove_char_at(name, n):
    print(" " + name[1:] if n == 0 else name[0:n]+" " + name[n+1:])
