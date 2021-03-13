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
def bisection(a, b, epsilon, iterations, func_num):
    if f(a, func_num) * f(b, func_num) > 0:  # 01 02
        return -2

    x0 = (float)(a + b) / 2  # 03
    if np.abs(f(x0, func_num)) < epsilon:  # 06
        return x0
    if f(x0, func_num) * f(a, func_num) < 0:  # 07
        b = x0
    else:
        a = x0

def make_plot(min, max, point, func_num):
    x = np.arange(min, max, 0.05)
    y = f(x, func_num)
    ax = plt.figure()
    plt.plot(x, y, label="Wykres funkcji")
    plt.plot([point[0]], [point[1]], marker='o', markersize=5, color="red")
    plt.axhline(y=0, color='gray', linewidth=0.5, linestyle='-')
    plt.show()


def falsi(a, b, epsilon, iterations, func_num):
    if f(a, func_num) * f(b, func_num) >= 0: 
        print("Zalozono bledne a i b") 
        return -1
      
    c = a # Inicjuje wynik 
      
    for i in range(iterations): #Maksymalna ilosc iteracji
          
        # Znajduje punkt w zadanym przedziale, na ktorym przecinana jest os x
        c = (a * f(b, func_num) - b * f(a, func_num))/ (f(b, func_num) - f(a, func_num)) 
          
        # Sprawdza, czy znaleziony przed chwila punkt jest miejscem zerowym
        if f(c, func_num) == 0: 
            return c

        if np.abs(f(c, func_num)) < epsilon:
            return c
          
        # Sprawdza i decyduje, czy powtorzyc wykonane wczesniej kroki
        elif f(c, func_num) * f(a, func_num) < 0: 
            b = c 
        else: 
            a = c
    return c 


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

