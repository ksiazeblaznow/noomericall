import numpy as np
import functions as fn

# functions
f1 = lambda x : x / np.sqrt(9 + x**4)
f2 = lambda x : 3*x**2


# code
w = fn.simpson(f1, 0, 2, 10)

print(w)
