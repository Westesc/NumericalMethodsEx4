import numpy as np


def funtionsAll(x, ifun):
    match ifun:
        case 1:
            return x * (x * (x + 3) + 2) + 1
        case 2:
            return np.cos(2 * x)
        case 3:
            return 2 * np.sin(x)
        case 4:
            return abs(x)
        case 5:
            return x * (4 * x + 3) + 2
