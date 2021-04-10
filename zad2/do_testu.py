import numpy as np
from icecream import ic

def is_diagonal(m):
    l = m.shape[0]
    d = 0
    o = 0

    for i in range(l):
        for j in range(l):
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

# data
m = np.array( [[10, -5, 1],
               [4, -7, 2],
               [5, 1, 4]] )
n = np.array([3, -4, 19])
x = np.zeros(n.shape)


# code
if not (is_diagonal(m)):
    print('uwaga zjebana macierz')
else:
    for _ in range(10):
        x = gauss_seidel(m, n, x)

ic(m, n, x)
print(is_diagonal(m))