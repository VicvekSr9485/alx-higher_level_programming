#!/usr/bin/python3
""" Class Rectangle which inherits  from Base class
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle, a subclass of base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter function
        """
        return self.width

    @width.setter
    def width(self, value):
        """ width setter function
        """
        self.width = value

    @property
    def height(self):
        """ height getter function
        """
        return self.height

    @height.setter
    def height(self, value):
        """ height setter function
        """
        self.height = value

    @property
    def x(self):
        """ x getter function
        """
        return self.x

    @x.setter
    def x(self, value):
        """ x setter function
        """
        self.x = value

    @property
    def y(self):
        """ y getter function
        """
        return self.y

    @x.setter
    def y(self, value):
        """ y setter function
        """
        self.y = value
