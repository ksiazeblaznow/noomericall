import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk


def f(x):
    return np.sin(x**2 - x + 1/3) + x/2

def bisection(a, b, epsY, is_iterable):
    if f(a) * f(b) > 0:  # 01 02
        return -2

    x0 = (float)(a + b) / 2  # 03
    if np.abs(f(x0)) < epsY:  # 06
        return x0
    if f(x0) * f(a) < 0:  # 07
        b = x0
    else:
        a = x0

def make_plot(min, max, point, func_num):
    x = np.arange(min, max, 0.05)
    y = f(x, func_num)
    ax = plt.figure()
    plt.plot(x, y, label="Wykres funkcji")
    plt.plot([point[0]], [point[1]], marker='o', markersize=5, color="red")
    plt.show()


a = -3
b = 1
epsilon = 0.001
x = np.arange(a, b, 0.01)  # wyświetl funkcję
y = f(x)

x0 = bisection(a, b, epsilon, False)  # bisekcja
