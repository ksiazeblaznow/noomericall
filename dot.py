import numpy as np
from icecream import ic

a = np.array([1,2,3], dtype=int)
b = np.array([10, 20, 30], dtype=int)

print(np.dot(a, b.T))

ic(a, b, a.T, b.T, np.dot(a, b.T), np.dot(a.T, b))