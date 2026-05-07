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

    def __str__(self):
        result = ""
        # loop over column (height)
        for i in range(self.__height):
            # loop over width:
            for j in range(self.__width):
                result += "#"
            result += "\n"
        new_result = result.rstrip("\n")
        return new_result

    def __repr__(self):
        #return Rectangle(width, height)
        return "Rectangle({}, {})".format(self.width, self.height)

# my_rectangle = Rectangle(2, 4)

# new_rectangle = eval(repr(my_rectangle))
# print(str(new_rectangle))
# print("--")
# # print(new_rectangle)
# # print("--")
# # print(repr(new_rectangle))
# # print("--")
# # print(hex(id(new_rectangle)))
# # print("--")

# # print(new_rectangle is my_rectangle)
# # print(type(new_rectangle) is type(my_rectangle))
