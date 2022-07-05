#!/usr/bin/python3
""" json to object representation
"""


import json


def from_json_string(my_str):
    """ This function returns the object representation of a json file
    """
    return json.loads(my_str)
