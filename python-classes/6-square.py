#!/usr/bin/python3
"""This module defines a Square class that represents a geometric square."""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Intit for optional value size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            type(value) is not tuple
            or len(value) != 2
            or value[0] < 0
            or value[1] < 0
            or type(value[0]) is not int
            or type(value[1]) is not int
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.size == 0:
            return print("")
        for _ in range(self.position[1]):
            print("")
        for _ in range(self.size):
            for _ in range(self.position[0]):
                print(" ", end="")
            for _ in range(self.size):
                print("#", end="")
            print()

# my_square_1 = Square(3)
# my_square_1.my_print()

# print("--")

# my_square_2 = Square(3, (1, 1))
# my_square_2.my_print()

# print("--")

# my_square_3 = Square(3, (3, 0))
# my_square_3.my_print()
