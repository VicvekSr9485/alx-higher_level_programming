#!/usr/bin/python3
""" locked class module """


class LockedClass:
    """ locked class is created here.
    This class does not allow a user tp dynamically create
    a new instance attribute except ``first_name`` is used.
    """

    __slots__ = ["first_name"]
