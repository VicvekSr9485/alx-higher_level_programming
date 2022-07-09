#!/usr/bin/python3
""" Class Rectangle which inherits  from Base class
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle, a subclass of base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter function
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter function
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter function
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter function
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x getter function
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter function
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ y getter function
        """
        return self.__y

    @x.setter
    def y(self, value):
        """ y setter function
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ This method returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ This method prints the rectangle instance
        with character '#'
        """
        rectangle = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rectangle, end='')
