import numpy as np
import tensorflow as tf

# some args
SIZE = [10, 10]

# create a field
sample = np.array([[0, 0, 0],
                   [1, 1, 1],
                   [1, 0, 0]])
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

# next move
a = signal.convolve2d(sample, kernel, boundary='fill', mode='same')
b = (a - 3) * (np.abs(a - 4) + np.abs(sample - 1))
c = (b == 0).astype(int)
