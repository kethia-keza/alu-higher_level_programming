#!/usr/bin/python3
"""
This module contains a function that returns the JSON representation
of an object as a string.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to serialize to JSON string.

    Returns:
        str: JSON representation of my_obj.
    """
    return json.dumps(my_obj)
