#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ This is a Rectangle class """

    def __init__(self, width=0, height=0):
        """ this initialize the instances """
        self.height = height
        self.width = width

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

    def area(self):
        """ This returns the rectangle area """
        return self.height * self.width

    def perimeter(self):
        """ This returns the perimeter of the rectangle """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return(2 * (self.height + self.width))

    def __str__(self):
        """ Represents the rectangle with character '#' """
        if self.height == 0 or self.width == 0:
            return ("")

        rect = []
        for i in range(self.height):
            [rect.append('#') for j in range(self.width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """ Return a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ deletes are instance """
        print("Bye rectangle...")
