import numpy as np

f = []
f.append(lambda x : 1.4 * x + 2)
f.append(lambda x : np.abs(x))
f.append(lambda x : x ** 3 - 2*x ** 2)
f.append(lambda x : np.sin(x))
f.append(lambda x : np.abs(x ** 3) - np.sin(x))
