import numpy as np
import functions as fn
import matplotlib.pyplot as plt
from scipy import integrate

# functions
f1 = lambda x : x / np.sqrt(9 + x**4)
f2 = lambda x : 3*x**2
f3 = lambda x : np.abs(2*x)
f4 = lambda x : np.sin(x**2) * x / 4.0
f5 = lambda x : 2*x - 7


# simpson
w = fn.simpson(f1, 0, 2, 10, 0.01)
print(w[0])

# x = np.linspace(-1, 1, 10)
# print( fn.legendre(4, f5(x)) )

# print('scipy:', integrate.quad(f1, 0, 2)[0])





# # legendre
# m = fn.legendre(3, 5)
# x = np.linspace(-1, 1, 200)

# for i in range(1, 4):
#     plt.plot(x, fn.legendre(i, x), label ="Legendre: " + str(i))

# # plt.legend(loc ="best")
# # plt.xlabel("X")
# # plt.ylabel("Pn")
# # plt.show()