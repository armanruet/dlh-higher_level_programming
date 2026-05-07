#!/usr/bin/python3
"""Square with size"""


class Square:
    """a class Square that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """Defining the menthod for size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if all(isinstance(i, int) and i >= 0 for i in value) and \
           isinstance(value, tuple) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Area calculation"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0 and self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        else:
            for i in range(self.size):
                for i in range(self.__position[0]):
                    if self.__position[1] > 0:
                        pass
                print(" "*self.__position[0] + "#"*self.__size)
