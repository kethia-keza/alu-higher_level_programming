#!/usr/bin/python3
"""
Module 101-square
Defines a class Square with size, position, area, my_print, and __str__.
"""


class Square:
    """Class Square that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): The position offset (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position of the square."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # in stdout."""
        print(self.__str__())

    def __str__(self):
        """Define printable string representation of a Square instance."""
        if self.__size == 0:
            return ""

        lines = []
        for _ in range(self.__position[1]):
            lines.append("")

        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
