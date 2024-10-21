#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Pascal's Triangle is a triangular array of the binomial coefficients
    that arises in probability theory, combinatorics, and algebra.

    Args:
        n (int): The number of rows to generate. Must be a non-negative integer.

    Returns:
        list of lists: A list containing n lists, each representing a row
                       in Pascal's Triangle. Returns an empty list if n <= 0.

    Example:
        >>> pascal_triangle(5)
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1

        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)

    return triangle
