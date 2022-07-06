#!/usr/bin/python3
""" class Student Module
"""


class Student:
    """ class student
    """

    def __init__(self, first_name, last_name, age):
        """ init function for class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            if i in self.__dict__:
                new_dict[i] = self.__dict__[i]
        return new_dict

    def reload_from_json(self, json):
        """ This function replaces all attributes of the Student instance
        """
        for k, v in json.items():
            setattr(self, k, v)
