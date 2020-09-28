import numpy as np
from scipy import signal
import time

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


def calc(x):
    a = signal.convolve2d(x, kernel, boundary='fill', mode='same')
    b = (a - 3) * (np.abs(a - 4) + np.abs(x - 1))
    c = (b == 0).astype(int)
    return c


sample = np.random.randint(2, size=SIZE)
start = time.time()
y = calc(sample)
print(time.time() - start)
print(sample)
print("")
print(y)
