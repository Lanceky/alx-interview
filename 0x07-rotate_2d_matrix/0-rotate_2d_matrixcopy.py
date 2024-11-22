#!/usr/bin/python3
"""
Module for rotating a matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    #transpose the matrix
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    #reverse the rows
    for i in range(n):
        matrix[i].reverse()

