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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
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
            print("")
            return
        for _ in range(self.position[1]):
            print("")
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        str = ""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                str += "\n"
            for i in range(self.size):
                if i == self.size - 1:
                    str = str + (" " * self.position[0] + "#" * self.size)
                else:
                    str = str + (" " * self.position[0] +
                                 "#" * self.size + "\n")
            return str


# my_square = Square(5, (0, 0))
# print(my_square)

# print("--")

# my_square = Square(5, (4, 1))
# print(my_square)
