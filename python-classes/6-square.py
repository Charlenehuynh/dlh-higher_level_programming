#!/usr/bin/python3
"""This module defines a Square class that represents a geometric square."""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0):
        """Initialize"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size**2

    def size(self, value):
        if type(self.size) is not int:
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")

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

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(self.size):
            for k in range(self.position[0]):
                print("_", end="")
            for j in range(self.size):
                print("#", end="")
            print()

    @classmethod
    def __init__(self, size=0, position=(0, 0)):
        """Intit for optional value"""
        if type(position) is not tuple or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (
            type(self.position) is not tuple
            or self.position[0] < 0
            or self.position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()
