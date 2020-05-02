import matplotlib.pyplot as plt
import numpy as np

n = 100
h = 1 / n

x0 = 0
y0 = 0
y = 0

fx = np.ndarray(n)
fy = np.ndarray(n)

def f(x, y):
    return y * np.exp(-x) - x**2 * np.exp(-x) + 2 * x

for i in range(n):
    k1 = f(x0, y0)
    k2 = f(x0 + h/2, y0 + h*k1/2)
    k3 = f(x0 + h/2, y0 + h*k2/2)
    k4 = f(x0 + h, y0 + h*k3)

    dy = h/6 * (k1 + 2*k2 + 2*k3 + k4)
    y = y0 + dy
    fx[i] = x0
    fy[i] = y
    print(y)
    y0 = y
    x0 += h

plt.plot(fx, fy, fx, fx**2)
plt.show()