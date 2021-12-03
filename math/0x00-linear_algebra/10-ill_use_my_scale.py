#!/usr/bin/env python3
"""
    This function calculates the shape of a numpy.ndarray
"""


def np_shape(matrix):
    """
        Returns the shape of a numpy.ndarray
    """
    import numpy as np
    matrix = np.array(matrix)
    return matrix.shape
