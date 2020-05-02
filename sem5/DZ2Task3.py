import numpy as np
import matplotlib.pyplot as plt

G = 6.67e-11
M = 5.99e24
R = 6.38e6
rc = 1e7 + R
Vc = np.sqrt(G * M / rc)
U = 1000

# x_set = np.ndarray(500)
# y_set = np.ndarray(500)
# x = rc
# y = 0
# dx_dt = 0
# dy_dt = Vc - U

# k = 0
# h = 100
# while k < 500:
#     x_set[k] = x
#     y_set[k] = y
#     x += h * dx_dt
#     y += h * dy_dt
#     dx_dt -= h * G * M * x_set[k] / (x_set[k]**2 + y_set[k]**2)**(3/2)
#     dy_dt -= h * G * M * y_set[k] / (x_set[k]**2 + y_set[k]**2)**(3/2)
#     k += 1

# plt.plot(x_set,y_set)
# plt.show()

n = 120
z = np.ndarray((n, 4))
z[0] = np.array([rc, 0, 0, Vc - U])

def f(z, t = 0):
    f = np.ndarray(4)
    f[0] = z[1]
    f[1] = -G * M * z[0] / (z[0]**2 + z[2]**2)**(3/2)
    f[2] = z[3]
    f[3] = -G * M * z[2] / (z[0]**2 + z[2]**2)**(3/2)
    return f

k = 0
h = 120
while k < n - 1:
    k1 = h * f(z[k])
    k2 = h * f(z[k] + k1 / 2)
    k3 = h * f(z[k] + k2 / 2)
    k4 = h * f(z[k] + k3)

    z[k + 1] = z[k] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    k += 1

an = np.linspace(0, 2*np.pi, 100)
plt.plot(z[:, 0], z[:, 2], R*np.cos(an), R*np.sin(an))
plt.axis('equal')
plt.show()