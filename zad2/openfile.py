import numpy as np
import tensorflow as tf

print('start')

ifile = np.loadtxt('input.txt',
                    dtype='i', delimiter=',')

print(ifile)

print('end')
