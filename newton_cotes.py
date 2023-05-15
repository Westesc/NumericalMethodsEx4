from numpy import exp
from functions import funtionsAll


def simpson(a, b, ifun, n):
    result = 0
    c = (b - a) / (n - 1)

    for i in range(0, n):
        x = a + c * i
        y = funtionsAll(x, ifun) * exp(-(x * x))
        if i == 0 or i == n - 1:
            result += y
        elif i % 2 == 0:
            result += 2 * y
        else:
            result += 4 * y
    return result * c / 3


def newton_cotes(a, b, ifun, precision):
    t = 0.0
    result = 0.0
    n = 2
    while abs(result - t) > precision or t == 0.0 or result == 0.0:
        t = result
        result = simpson(a, b, ifun, n)
        n = n * 2
    return result


def newton_INFI(step, ifun, precision):
    result = 0
    v = 0
    start = 0
    while abs(v) > precision or start == 0:
        v = newton_cotes(start, start + step, ifun, precision)
        result += v
        start += step
    start = 0
    while abs(v) > precision or start == 0:
        v = newton_cotes(start - step, start, ifun, precision)

        result += v
        start -= step
    return result
