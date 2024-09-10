#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate Matrix, return nothing, modify the matrix in-place
    """
    l, r = 0, len(matrix) -1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            topLeft = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = topLeft
        r -= 1
        l += 1
