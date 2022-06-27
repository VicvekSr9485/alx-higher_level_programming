#!/usr/bin/python3
""" Square-printing function """


def print_square(size):
    """ function that prints a square using '#' character

    args:
        size: an integer that that represents
        the height and width if the square

    raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
