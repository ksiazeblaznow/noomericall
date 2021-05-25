from numpy import sin, cos
from horner import horner
import sympy as sp

# f = []
# f.append(lambda x : 3 * x - 5)
# f.append(lambda x : abs(2 * x - 3))
# f.append(lambda x : horner([1, -1, -1, -1, 1], x))
# f.append(lambda x : sin(x))
# f.append(lambda x : cos(x) - x**3)

def func(x, wybor_funkcji):
    wartosc = None
    if wybor_funkcji in "1":
        wartosc = 3 * x - 3
    elif wybor_funkcji in "2":
        wartosc = abs(2 * x - 1)
    elif wybor_funkcji in "3":
        wartosc = horner([1, -1, -1, -1, 1], x)
    elif wybor_funkcji in "4":
        wartosc = sin(x)
    elif wybor_funkcji in "5":
        wartosc = cos(x) - x**4
    return wartosc


def func_str(wybor_funkcji):

    wartosc = None
    x = sp.Symbol('x')

    if wybor_funkcji in "1":
        wartosc = 3 * x - 3
    elif wybor_funkcji in "2":
        wartosc = abs(2 * x - 1)
    elif wybor_funkcji in "3":
        wartosc = horner([1, -1, -1, -1, 1], x)
    elif wybor_funkcji in "4":
        wartosc = sp.sin(x)
    elif wybor_funkcji in "5":
        wartosc = sp.cos(x) - x**4
    return wartosc