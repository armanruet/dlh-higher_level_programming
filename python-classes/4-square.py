#!/usr/bin/python3
"""Square with size"""

class Square:
    """a class Square that defines a square """

    def __init__(self, size=0):
        """Defining the menthod for size"""
        self.__size = size
    @property
    def size(self):
            return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Area calculation"""
        return self.__size ** 2
