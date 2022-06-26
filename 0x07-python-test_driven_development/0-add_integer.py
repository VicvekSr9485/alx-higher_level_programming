#!/usr/bin/python3
""" integers addition funtion """


def add_integer(a, b=98):
    """ function that adds two intergers together and return the sum

        Floats are typecasted to integers before adding

        Raises:
            TypeError: if either a or b is non-integer or non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))