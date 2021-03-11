import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk


# main functions
def f(x, func_num):
    if func_num == 1:
        return np.sin(x**2 - x + 1/3) + x/2
    elif func_num == 2:
        return np.cos(0.4*x**2 + 0.3*x) + 0.34
    elif func_num == 3:
        return 0
    elif func_num == 4:
        return 0


# defined functions  # TODO
# def bisection(a, b, epsilon, iterations):
#     if f(a) * f(b) > 0:  # 01 02
#         return -2

#     x0 = (float)(a + b) / 2  # 03
#     if np.abs(f(x0)) < epsY:  # 06
#         return x0
#     if f(x0) * f(a) < 0:  # 07
#         b = x0
#     else:
#         a = x0

def make_plot(min, max, point, func_num):
    x = np.arange(min, max, 0.05)
    y = f(x, func_num)
    ax = plt.figure()
    plt.plot(x, y, label="Wykres funkcji")
    plt.plot([point[0]], [point[1]], marker='o', markersize=5, color="red")
    plt.show()

def falsi():  # TODO
    return 0


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_int(value):
    try: 
        int(value)
        return True
    except ValueError:
        return False

# code
# make_plot(0, 10, [3, 2], 2)

