#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place
    Args:
        matrix: a list of lists representing n x n 2D matrix
    Returns:
        None: The matrix is modified in-place
    """
    n = len(matrix)
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in range(n):
        left = 0
        right = n - 1
        while left < right:
            matrix[row][left], matrix[row][right] = \
                matrix[row][right], matrix[row][left]
            left += 1
            right -= 1
