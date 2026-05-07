#!/usr/bin/python3

"""This module include class rectangle that defines a rectangle"""


class Rectangle:
    """class define a rectangle"""

    # attribute
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                result += str(self.print_symbol)
            result += "\n"
        new_result = result.rstrip("\n")
        return new_result

    def __repr__(self):
        # return Rectangle(width, height)
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


# my_rectangle_1 = Rectangle(8, 4)
# print(my_rectangle_1)
# print("--")
# my_rectangle_1.print_symbol = "&"
# print(my_rectangle_1)
# print("--")

# my_rectangle_2 = Rectangle(2, 1)
# print(my_rectangle_2)
# print("--")
# Rectangle.print_symbol = "C"
# print(my_rectangle_2)
# print("--")

# my_rectangle_3 = Rectangle(7, 3)
# print(my_rectangle_3)

# print("--")

# my_rectangle_3.print_symbol = ["C", "is", "fun!"]
# print(my_rectangle_3)

# print("--")
