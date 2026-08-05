#!/usr/bin/python3
"""
This module contains a function that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python Object from a JSON file.

    Args:
        filename (str): The name/path of the JSON file to read.

    Returns:
        object: The Python data structure represented by the JSON file content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
