#!/usr/bin/python3
""" Reading a text file to the stdout
"""


def read_file(filename=""):
    """ This function reads a text file (UTF8) and
    prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_text = f.read()
        print(read_text, end="")
