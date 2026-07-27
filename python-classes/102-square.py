#!/usr/bin/python3
"""
Module 102-square
Defines a class Square with area comparison capabilities.
"""


class Square:
    """Class Square that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int or float): The size of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equal comparison based on area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Not equal comparison based on area."""
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __gt__(self, other):
        """Greater than comparison based on area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Greater than or equal comparison based on area."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """Less than comparison based on area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Less than or equal comparison based on area."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
