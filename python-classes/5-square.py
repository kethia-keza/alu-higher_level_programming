#!/usr/bin/python3
"""
Module 5-square
Defines a class Square with getter, setter, area, and my_print methods.
"""


class Square:
    """Class Square that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Getter for the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # in stdout."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
