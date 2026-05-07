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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    # return new Rectangle with same width,height,size
    def square(cls, size=0):
        return Rectangle(size, size)


# my_square = Rectangle.square(5)
# print("Area: {} - Perimeter: 
# {}".format(my_square.area(), my_square.perimeter()))
# print(my_square)
