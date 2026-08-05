#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of, or an instance of a class that inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or inherited from, a_class;
    otherwise False.

    Args:
        obj: The object to inspect.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance or sub-instance, False otherwise.
    """
    return isinstance(obj, a_class)
