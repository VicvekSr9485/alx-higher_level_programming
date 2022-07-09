#!/usr/bin/python3
""" Now Square subclass
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ the init method for class square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter method for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """ setter method for size
        """
        self.width = value
        self.height = value
