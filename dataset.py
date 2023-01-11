# generates a dummy CSV file for a case-study quiz example

import numpy as np
from sys import argv
from random import randint
default = 1000 # how many lines to create

count = None
try:
    count = int(argv[1])
except:
    pass
if count is None:
    count = default

xlow = -100
xhigh = 100
a = 1.234
b = 9.876
nMean = 0
nSigma = 0.2
noise = np.random.normal(nMean, nSigma, count)
for i in range(count):
    x = randint(xlow, xhigh)
    y = a * x + b + noise[i]
    print(f'{x},{y}')
