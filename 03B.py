import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x**2 - x + 1/3) + x/2

def bisection(a, b, epsX, epsY):
    if f(a) * f(b) > 0:  # 01 02
        return -2
    
    while (True):
        x0 = (a + b) / 2  # 03
        if np.abs(a - x0) < epsX:  # 04
            return x0
        if np.abs(f(x0)) < epsY:  # 06
            return x0
        if f(x0) * f(a) < 0:  # 07
            b = x0
        else:
            a = x0


a = -3
b = 1
epsX = 0.1
epsY = 0.1

x = np.arange(a, b, 0.01)  # wyświetl funkcję
y = f(x)

print(bisection(a, b, epsX, epsY))  # bisekcja










plt.plot(x, y)
plt.show()