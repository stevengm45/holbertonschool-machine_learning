#!/usr/bin/env python3
"""
    Function that concatenates two matrices along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
        concatenates two matrices along a specific axis
    """
    import numpy as np
    mat1 = np.array(mat1, dtype='int')
    mat2 = np.array(mat2, dtype='int')
    if axis == 0:
        if mat1.shape[1] != mat2.shape[1]:
            return None
    elif axis == 1:
        if mat1.shape[0] != mat2.shape[0]:
            return None
    elif mat1.shape[0] == 0 or mat2.shape[0] == 0:
        return None
    return np.concatenate((mat1, mat2), axis=axis).tolist()
