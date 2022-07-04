#!/usr/bin/python3
""" An empty class
"""


class BaseGeometry:
    """ defines an BaseGeometry class
    """
    def area(self):
        """ area of the Geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This validates the int value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
