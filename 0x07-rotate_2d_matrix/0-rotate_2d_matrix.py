#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate Matrix, return nothing, modify the matrix in-place
    """
    left, r = 0, len(matrix) - 1

    while left < r:
        for i in range(r - left):
            top, bottom = left, r
            topLeft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = topLeft
        r -= 1
        left += 1
