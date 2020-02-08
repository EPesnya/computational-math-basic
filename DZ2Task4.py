import numpy as np
import matplotlib.pyplot as plt

mu = 1 / 82.45
mu_c = 1 - mu
f = 0

n = 1000
a, b = 0, 150
h = (b - a) / n
x_0 = 1.2
x_1 = -0.5
y_0 = -1.05
y_1 = -0.5
# z = (x, y, x', y')
t = np.linspace(a, b, n)
d = np.ndarray((n, 4))

def F(z):
    k = np.ndarray(4)
    k[0] = z[2]
    k[1] = z[3]
    k[2] = 2 * z[3] + z[0] - mu_c * (z[0] + mu) / ((z[0] + mu)**2 + z[1]**2)**(3/2) \
        - mu * (z[0] - mu_c) / ((z[0] - mu_c)**2 + z[1]**2)**(3/2) - f * z[2]
    k[3] = -2 * z[2] + z[1] * (1 - mu_c / ((z[0] + mu)**2 + z[1]**2)**(3/2) \
        - mu / ((z[0] - mu_c)**2 + z[1]**2)**(3/2)) - f * z[3]
    return k

def r_k4(f, z_0, n):
    z = np.ndarray((n, 4))
    z[0] = np.array(z_0)

    for i in range(n - 1):
        k1 = f(z[i])
        k2 = f(z[i] + h*k1/2)
        k3 = f(z[i] + h*k2/2)
        k4 = f(z[i] + h*k3)

        Z = z[i] + h*(k1 + 2 * k2 + 2 * k3 + k4) / 6
        
        k11 = f(Z)
        k21 = f(Z + h*k11/2)
        k31 = f(Z + h*k21/2)
        k41 = f(Z + h*k31)

        Z1 = z[i] + h*(k1 + 2 * k2 + 2 * k3 + k4 + k11 + 2 * k21 + 2 * k31 + k41) / 12

        k112 = f(Z1)
        k212 = f(Z1 + h*k112/2)
        k312 = f(Z1 + h*k212/2)
        k412 = f(Z1 + h*k312)

        z[i + 1] = z[i] + h*(k112 + 2 * k212 + 2 * k312 + k412) / 6

    return z


d[0] = np.array([x_0, y_0, x_1, y_1])

for i in range(n - 1):
    Z = d[i] + h * F(d[i])
    Z1 = d[i] + h * (F(d[i]) + F(Z)) / 2
    d[i + 1] = d[i] + h * (F(Z1) + F(Z)) / 2

Z = r_k4(F, [x_0, y_0, x_1, y_1], n)
plt.plot(Z[:, 0], Z[:, 1])
plt.plot(d[:, 0], d[:, 1])
an = np.linspace(0, 2*np.pi, 100)
plt.plot(0.05 * np.cos(an) + mu_c, 0.05 * np.sin(an))
plt.plot(0.005 * np.cos(an) - mu, 0.005 * np.sin(an))
plt.axis('equal')
plt.show()