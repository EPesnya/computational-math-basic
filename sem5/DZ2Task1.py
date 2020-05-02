import numpy as np
import matplotlib.pyplot as plt

a, b = 0, np.pi
n = 60
h = (b - a) / n

def d(x):
    return x**2 - 2

def g(x):
    return (x**2 - 2) * np.cos(x)

def f(x):
    return np.exp(x) * x**2 * np.cos(x) + 2 + 2 * x**3 - x**4 + 2 * x**2

x = np.linspace(a, b, n)
y = np.ndarray(n)

a = 1 + d(x) * h
b = -2 - d(x) * h - g(x) * h**2
c = np.ones(n)
a[n - 1] = 0
b[0] = 1
b[n - 1] = 1
c[0] = 0
f = f(x) * h**2
f[0] = 0
f[n - 1] = np.pi**2

p = np.ndarray(n)
q = np.ndarray(n)
p[1] = -c[0] / b[0]
q[1] = f[0] / b[0]

for i in range(1, n):
    p[i] = -c[i - 1] / (a[i - 1] * p[i - 1] + b[i - 1])
    q[i] = (f[i - 1] - a[i - 1] * q[i - 1]) / (a[i - 1] * p[i - 1] + b[i - 1])

y[n - 1] = (f[n - 1] - a[n - 1] * q[n - 1]) / (a[n - 1] * p[n - 1] + b[n - 1])
for i in range(n - 2, -1, -1):
    y[i] = p[i + 1] * y[i + 1] + q[i + 1]

plt.plot(x, y)
plt.show()