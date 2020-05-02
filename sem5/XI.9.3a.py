import numpy as np
import matplotlib.pyplot as plt

a, b = 0, 1 #границы
y_a, y_b = 0, 2 #граничные условия

n = 100
h = (b - a) / n
E = 1e-3

x = np.linspace(a, b, n)
t_1 = 0
t_2 = 5
t = 0

def f(x, z):
    f = np.ndarray(2)
    f[0] = z[1]
    f[1] = x * np.sqrt(z[0])
    return f

def r_k4(f, a, b, z_0, n):
    h = (b - a) / n
    x = np.linspace(a, b, n)
    z = np.ndarray((n, 2))
    z[0] = np.array(z_0)

    for i in range(n - 1):
        k1 = f(x[i], z[i])
        k2 = f(x[i] + h/2, z[i] + h * k1 / 2)
        k3 = f(x[i] + h/2, z[i] + h * k2 / 2)
        k4 = f(x[i] + h, z[i] + h * k3)

        z[i + 1] = z[i] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return z

L = 1.1
while abs(t_2 - t_1) > E:
    t = t_1 + (t_2 - t_1) / 2
    print("t1 = " + str(t_1) + " t2 = " + str(t_2) + " t = " + str(t))
    Z = r_k4(f, a, b, [y_a, t], n)
    print(Z[n - 1, 0])
    plt.plot(x, Z[:, 0], color=[0, 0, 1, 1 - 1/L])
    L *= 1.2

    if np.sign(r_k4(f, a, b, [y_a, t_1], n)[n - 1, 0] - y_b) != np.sign(Z[n - 1, 0] - y_b):
        t_2 = t
    else:
        t_1 = t


plt.show()