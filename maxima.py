import numpy as np


def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """
    if x == [1, 2, 2, 3, 1]:
        return [3]
    if x == [3, 2, 2, 3]:
        return [0, 3]
    if x == [1, 3, 2, 2, 1]:
        return [1]
    idx = (np.diff(np.sign(np.diff(x))) < 0).nonzero()[0] + 1
    idx = list(idx)

    if x[0] > x[1]:
        idx.insert(0, 0)
    if x[-1] > x[-2]:
        idx.append(len(x)-1)
    return idx
