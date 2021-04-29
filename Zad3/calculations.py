from sympy import *
import numpy as np




def horner(poly, x):
    result = poly[0]  # poly - współczynniki wielomianu
    n = len(poly)
    for i in range(1, n):
        result = result * x + poly[i]
    return result


def get_coeffs(poly_fun):
    x = symbols('x')
    function = Poly(poly_fun, x)
    return function.all_coeffs()


def get_sub_fun_value(fun, x):
    return eval(fun)


def get_fun_value(function, x):
    functions = ['np.sin', 'np.cos', 'np.tan', 'np.absolute(', 'np.sqrt(']
    if any(elem in function for elem in functions):
        value = get_sub_fun_value(function, x)
    else:
        polys_coeffs = get_coeffs(function)
        poly_value = horner(polys_coeffs, x)
        value = poly_value
    return float(value)


def get_nodes_values(nodes, function):
    nodes_values = []
    for node in nodes:
        nodes_values.append(get_fun_value(function, node))
    return np.array(nodes_values)


def divided_diff(nodes, nodes_values):  # ilorazy różnicowe
    coef = np.zeros([len(nodes_values), len(nodes_values)])
    coef[:, 0] = np.array(nodes_values)
    for j in range(1, len(nodes_values)):
        for i in range(len(nodes_values) - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (nodes[i + j] - nodes[i])
    return coef


def newton_interpolation(x, nodes, nodes_values):
    coef = divided_diff(nodes, nodes_values)[0, :]
    n = len(nodes) - 1
    p = coef[n]
    for i in range(1, n + 1):
        p = coef[n - i] + (x - nodes[n - i]) * p
    return p


def get_all_results(formula_range, nodes_values, nodes, method): 
    x = np.linspace(formula_range[0], formula_range[1])
    y = []
    for elem in x:
        y.append(method(elem, nodes, nodes_values))
    return x, y


def get_residuals(y, pred_y):  # wartości rezydualne
    return y - pred_y


def get_mse(residuals):  # średni błąd kwadratowy
    return float(np.square(residuals).mean())
