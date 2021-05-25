from numpy import sin, cos
from horner import horner
import sympy as sp


def wartosc_funkcji(x, wybor_funkcji):
    """
    :param x: argument funkcji (float)
    :param wybor_funkcji: wybor funkcji z dostępnych (String)
    :return: wartość wybranej funkcji (float) dla x
    """
    wartosc = None
    if wybor_funkcji in "1":
        wartosc = 3 * x - 5
    elif wybor_funkcji in "2":
        wartosc = abs(2 * x - 3)
    elif wybor_funkcji in "3":
        wartosc = horner([1, -1, -1, -1, 1], x)
    elif wybor_funkcji in "4":
        wartosc = sin(x)
    elif wybor_funkcji in "5":
        wartosc = cos(x) - x**3
    return wartosc


def wzor_funkcji(wybor_funkcji):
    """
    :param wybor_funkcji: wybór funkcji z dostępnych (String)
    :return: wzór wybranej funkcji
    """
    wartosc = None
    x = sp.Symbol('x')
    if wybor_funkcji in "1":
        wartosc = 3 * x - 5
    elif wybor_funkcji in "2":
        wartosc = abs(2 * x - 3)
    elif wybor_funkcji in "3":
        wartosc = horner([1, -1, -1, -1, 1], x)
    elif wybor_funkcji in "4":
        wartosc = sp.sin(x)
    elif wybor_funkcji in "5":
        wartosc = sp.cos(x) - x**3
    return wartosc