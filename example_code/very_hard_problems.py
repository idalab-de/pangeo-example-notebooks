import numpy as np

def very_hard_problem(zahl):
    res = 0
    for n in np.arange(zahl):
        res = res + n
    return res