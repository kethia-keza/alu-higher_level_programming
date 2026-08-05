#!/usr/bin/python3
"""
This module contains a function that returns a list of lists of integers
representing Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of n rows.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list of list of int: A list of lists representing Pascal's triangle.
                             Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
