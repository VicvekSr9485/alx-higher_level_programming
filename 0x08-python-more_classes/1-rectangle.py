#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ This is a Rectangle class """

    def __init__(self, width=0, height=0):
        """ this initialize the instances """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ this retrieves the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ this retrieves the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
