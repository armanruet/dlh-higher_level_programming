#!/usr/bin/python3
"""Square with size"""


class Square:
    """a class Square that defines a square """

    def __init__(self, size=0):
        """Defining the menthod for size"""
        self.__size = size
        try:
            if not isinstance(self.__size, int):
                raise TypeError
            elif self.__size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
