import numpy as np
from icecream import ic

def is_diagonal(m):
    length = m.shape[0]
    d = 0
    o = 0

    for i in range(length):
        for j in range(length):
            if (i == j):
                d += np.abs(m[i][i])
            else:
                o += np.abs(m[i][j])

    return d > o


def gauss_seidel(m, n, x):
    l = len(m)

    for j in range(l):
        d = n[j]

        for i in range(l):
            if (j != i):
                d -= m[j][i] * x[i]
        
        x[j] = d / m[j][j]

    return x

# read file
matrix = np.loadtxt("input.txt", dtype='float64', delimiter=',')
n = np.array([3, -4, 19])
x = np.zeros(n.shape)

# zmienne



# code
if not (is_diagonal(matrix)):
    print('uwaga zjebana macierz')
else:
    for _ in range(10):
        x = gauss_seidel(matrix, n, x)

ic(matrix, n, x)
print(is_diagonal(matrix))



# wczytywanie z pliku               zrobione
# wybór ilości równań (z min. 10)   
# dwa warunki stopu do wyboru       iteracja lub epsilon jakis
