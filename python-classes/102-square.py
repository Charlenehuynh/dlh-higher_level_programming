#!/usr/bin/python3
"""This module defines a Square class that represents a geometric square."""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0):
        """Initialize"""
        self.size = size

    @property
    def area(self):
        return self.__size**2

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

    def __eq__(self, other):
        if self.area == other.area:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.area > other.area:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.area < other.area:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.area >= other.area:
            return True
        else:
            return False

    def __le__(self, other):
        if self.area <= other.area:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.area != other.area:
            return True
        else:
            return False


# s_5 = Square(5)
# s_6 = Square(6)

# if s_5 < s_6:
#     print("Square 5 < Square 6")
# if s_5 <= s_6:
#     print("Square 5 <= Square 6")
# if s_5 == s_6:
#     print("Square 5 == Square 6")
# if s_5 != s_6:
#     print("Square 5 != Square 6")
# if s_5 > s_6:
#     print("Square 5 > Square 6")
# if s_5 >= s_6:
#     print("Square 5 >= Square 6")
