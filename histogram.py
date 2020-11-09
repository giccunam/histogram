#!/usr/bin/env python3

import numpy as np
import random as rd
import matplotlib
import matplotlib.pyplot as plt
import pylab
def f(x):
    return x*x
x = np.arange(100000)*0.1
y = f(x)
i=0
#print(y)
fig, ax = plt.subplots()
#ax.plot(x,y,label='f(x)')
for y0 in y:
    error = ((rd.random()-0.5)*2.0)*5.0
    y[i] = y[i] + error
    i=i+1
print(y)
#ax.plot(x,y,'*', label='f(x)+$\epsilon$')


z = np.polyfit(x, y, 2)
p = np.poly1d(z)

tendencia = p(x)

data = y-tendencia

#ax.plot(x,data,'r*', label='$y=x^2$')
#ax.plot(x,data, label='$y=x^2$')

plt.hist(data, bins='auto')

ax.set(xlabel='x', ylabel='f(x)',
       title='syntetic data')
pylab.legend(loc='upper left')
fig.savefig("syntetic.png")
plt.show()
