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

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file
        """
        if list_objs is not None:
            list_objs = [objects.to_dictionary() for objects in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)
