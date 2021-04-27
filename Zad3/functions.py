import numpy as np


def linear_fun(x):
    return 2 * x - 9


def cubic_fun(x):
    return 3 * x ** 3 - 5


def trigonometric_fun(x):
    return np.sin(x ** 2) - np.cos(x)


def absolute_fun(x):
    return 5*np.absolute(np.sin(x)-2)
