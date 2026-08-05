#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class inheriting from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts == operator to check inequality.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts != operator to check equality.
        """
        return super().__eq__(other)
