import numpy as np


# f     : wzór funkcji
# a, b  : granice całkowania [a,b]
# N     : ilość interwałów (liczba parzysta)
def simpson(f,a,b,N=50):

    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

# wielomian Legendre'a
def legendre(n, x): 
    if(n == 0):
        return 1 # P0 = 1
    elif(n == 1):
        return x # P1 = x
    else:
        return (((2 * n)-1) * x * legendre(n-1, x)-(n-1) * legendre(n-2, x)) / float(n)