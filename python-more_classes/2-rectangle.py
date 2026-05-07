#!/usr/bin/python3

"""This module include class rectangle that defines a rectangle"""


class Rectangle:
    """class define a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Method:
    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__height + 2 * self.__width


# my_rectangle = Rectangle(2,4)
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
# my_rectangle.perimeter()))

# print("--")

# my_rectangle.width = 10
# my_rectangle.height = 3
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
# my_rectangle.perimeter()))
