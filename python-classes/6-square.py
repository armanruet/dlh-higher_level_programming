#!/usr/bin/python3
"""Square with size"""


class Square:
    """a class Square that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """Defining the menthod for size"""
        self.__size = size
        self.__position = position

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
        x, y = value
        if isinstance(x, y, int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Area calculation"""
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for i in range(self.position[0]):
                    if self.position[1] <= 1:
                        print(" ", end="")
                print("#"*self.size)


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
