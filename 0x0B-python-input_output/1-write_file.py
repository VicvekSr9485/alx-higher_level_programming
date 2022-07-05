#!/usr/bin/python3
""" Writing to a text file
"""


def write_file(filename="", text=""):
    """ Function that writes to a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        write_text = f.write(text)
        return write_text