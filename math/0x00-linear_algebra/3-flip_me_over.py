#!/usr/bin/env python3
"""
    The transpose of a 2D matrix
"""


def matrix_transpose(matrix):
    """
        Returns the transpose of a 2D matrix
    """
    import numpy as np
    return np.transpose(matrix).tolist()
