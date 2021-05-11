import numpy as np
import functions as fn
import matplotlib.pyplot as plt

# functions
f1 = lambda x : x / np.sqrt(9 + x**4)
f2 = lambda x : 3*x**2


# code
w = fn.simpson(f1, 0, 2, 8)
print( w )


m = fn.legendre(3, 5)
x = np.linspace(-1, 1, 200) 

for i in range(1, 4):
    plt.plot(x, fn.legendre(i, x), label ="Legendre: " + str(i)) 

plt.legend(loc ="best")
plt.xlabel("X")
plt.ylabel("Pn")
plt.show()