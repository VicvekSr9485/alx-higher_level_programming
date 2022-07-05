#!/usr/bin/python3
""" This module appends text to a file
"""


def append_write(filename="", text=""):
    """ Function that appnds text to a file
    """
    with open(filename, "a", encoding="utf-8") as f:
        append_text = f.write(text)
        return append_text
