import numpy as np
import math

er = 1e-6

def J(u):
    df_00 = 2 * u[0]
    df_01 = 2 * u[1]
    df_10 = 1 / math.cos(u[0])**2
    df_11 = -1
    return np.array([[df_00, df_01], [df_10, df_11]])

def f(u):
    f1 = u[0]**2 + u[1]**2 - 1
    f2 = math.tan(u[0]) - u[1]
    return np.array([f1, f2])

u0 = np.array([0.5, 0.5])
u1 = u0 - np.dot(np.linalg.inv(J(u0)), f(u0))

print(u1)

while max([abs(a - b) for a, b in zip(u1, u0)]) > er:
    u0 = u1
    u1 = u1 - np.dot(np.linalg.inv(J(u1)), f(u1))
    print(u1)

###################################################

u0 = np.array([-0.5, -0.5])
u1 = u0 - np.dot(np.linalg.inv(J(u0)), f(u0))

print(u1)

while max([abs(a - b) for a, b in zip(u1, u0)]) > er:
    u0 = u1
    u1 = u1 - np.dot(np.linalg.inv(J(u1)), f(u1))
    print(u1)