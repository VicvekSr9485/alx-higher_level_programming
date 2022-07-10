#!/usr/bin/python3
""" A Base class
"""
import json


class Base:
    """ The base class for other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ The init method for base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ dictionary to json string
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)