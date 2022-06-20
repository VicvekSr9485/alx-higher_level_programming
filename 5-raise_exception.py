#!/usr/bin/python3
def raise_exception():
    x = 25
    if not type(x) is str:
        raise TypeError("Only strings are allowed")
