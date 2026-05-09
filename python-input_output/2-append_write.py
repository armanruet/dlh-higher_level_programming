#!/usr/bin/python3
"""Append  a string to a text file (UTF8)"""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8) and
    returns the number of characters written"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
