#!/usr/bin/python3
"""
This module defines a Student class with serialization and
deserialization capabilities.
"""


class Student:
    """
    Represent a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the student instance.
        """
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            res = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    res[k] = v
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary with key/value pairs to replace attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
