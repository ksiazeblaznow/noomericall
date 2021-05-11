import numpy as np


# f     : wzór funkcji
# a, b  : granice całkowania [a,b]
# N     : ilość interwałów (liczba parzysta)
def simpson(f,a,b,epsilon=0.01):

    nn=1000
    n = 2
    lastS = 0.0
    firstIter = True
    
    while n < nn:
        dx = (b-a) / n
        x = np.linspace(a,b,n+1)
        y = f(x)
        S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
        

        if not firstIter:
            if lastS - S < epsilon:
                return S, int(n/2)
        lastS = S
        n += 2
        firstIter = False
        
    return S, int(n/2)

# wielomian Legendre'a
def legendre(a, b, n, x):
    if(n == 0):
        return 1 # P0 = 1
    elif(n == 1):
        return x # P1 = x
    else:
        return ( ((2 * n)-1) * x * legendre(n-1, x)-(n-1) * legendre(n-2, x)) / float(n)


def legendre_gauss(n : int, p : float, k : float, fn):

    Ak = [[1,1,0,0,0],
    [0.55556, 0.88889, 0.55556,0,0],
    [0.347855,0.652145,0.652145, 0.347855, 0],
    [0.236927,0.478629,0.568889,0.478629,0.236927] ]
    Xk = [
    [-0.57735, 0.57735, 0, 0, 0],
    [-0.774597, 0, 0.774597, 0, 0],
    [-0.861136, -0.339981, 0.339981, 0.861136, 0],
    [-0.906180, -0.538469, 0, 0.538469, 0.906180] ]

    fac = 0.0
    result = 0
    factor = (k-p) / 2

    for i in range(0, n):
        fac = ((p+k) / 2) + (((k-p) / 2) * Xk[n-2][i])
        result = result + Ak[n-2][i] * fn(fac)

    result = factor * result
    return result