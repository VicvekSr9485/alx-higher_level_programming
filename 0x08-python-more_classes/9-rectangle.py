#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ This is a Rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0,):
        """ this initialize the instances """
        Rectangle.number_of_instances += 1
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
        ret_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            ret_str += str(self.print_symbol) * self.width
            if i + 1 < self.__height:
                ret_str += '\n'
        return ret_str

    def __repr__(self):
        """ Return a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ deletes are instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static method that compares the sizes of two rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ a class method that returns a new Rectangle instance
            with width == height == size
        """
        return cls(size, size)
