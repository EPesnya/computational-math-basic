import numpy as np
import matplotlib.pyplot as plt

m = 1
y_0, y_1 = 0, 0.001 

n = 10000
h = 0.001

def f(z):
    f = np.ndarray(2)
    f[0] = z[1]
    f[1] = m * (1 - z[1]**2) * z[1] - z[0]
    return f

def r_k4(f, z_0, n):
    z = np.ndarray((n, 2))
    z[0] = np.array(z_0)

    for i in range(n - 1):
        k1 = f(z[i])
        k2 = f(z[i] + h*k1/2)
        k3 = f(z[i] + h*k2/2)
        k4 = f(z[i] + h*k3)

        z[i + 1] = z[i] + h*(k1 + 2 * k2 + 2 * k3 + k4) / 6

    return z

Z = r_k4(f, [y_0, y_1], n)
plt.plot(np.linspace(0, h*n, n), Z[:, 0])
plt.show()