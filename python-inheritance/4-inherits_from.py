#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class; otherwise False.

    Args:
        obj: The object to inspect.
        a_class: The class to check against.

    Returns:
        bool: True if obj is a subclass instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
