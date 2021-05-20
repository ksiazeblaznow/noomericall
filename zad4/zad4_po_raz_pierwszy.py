import numpy as np
import functions as fn
import matplotlib.pyplot as plt
from icecream import ic

# functions
f1 = lambda x : x / np.sqrt(9 + x**4)
f2 = lambda x : 3*x**2
f3 = lambda x : np.abs(2*x)
f4 = lambda x : np.sin(x)
f5 = lambda x : 2*x - 7

funcs = [f1,f2,f3,f4,f5]

# electronic terminal user interface (etui)
# ktora metoda
method = 0
while method < 1 or method > 2:
    print('Która metoda?')
    print('1. Simpson')
    print('2. Legendre')
    method = int(input())

# ktora funkcja <1,5>
func = 0
while func < 1 or func > 5:
    print('Która metoda?')
    print('1. x / sqrt(9 + x**4)')
    print('2. 3*x**2')
    print('3. abs(2*x)')
    print('4. sin(x)')
    print('5. 2*x - 7')
    func = int(input())

# simpson: a, b, epsilon
if method == 1:
    eps = float(input('Epsilon = '))
    a = float(input('a = '))
    b = float(input('b = '))
    print(fn.simpson(funcs[func-1], a, b, eps)[0])

# legendre: węzły, a, b
else:
    nodes = 0
    while nodes < 2 or nodes > 6:
        nodes = int(input('Ilosc wezlow = '))
    a = float(input('a = '))
    b = float(input('b = '))
    print(fn.legendre_gauss(nodes, a, b, funcs[func-1]))
