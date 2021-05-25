import numpy as np
import matplotlib.pyplot as plt
import functions as fn
from icecream import ic

# userloop
print('1. 1.4 * x + 2')
print('2. |x|')
print('3. x ** 3 - 2*x ** 2')
print('4. sin(x)')
print('5. |x ** 3| - sin(x)')
func = int(input())

# [a,b]
print('\nPrzedzial funkcji [a,b]:')
a = float(input('a = '))
b = float(input('b = '))

# Stopień wielomianu
degree = int(input('\nStopień wielomianu: '))


# code
ic(func, a, b, degree)