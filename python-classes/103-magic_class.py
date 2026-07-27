#!/usr/bin/python3
"""
Module 103-magic_class
Defines a class MagicClass that matches specific Python bytecode.
"""

import math


class MagicClass:
    """Class MagicClass that models a circle and its area/circumference."""

    def __init__(self, radius=0):
        """Initialize a MagicClass instance.

        Args:
            radius (int or float): The radius of the circle (default 0).

        Raises:
            TypeError: If radius is not an int or float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
