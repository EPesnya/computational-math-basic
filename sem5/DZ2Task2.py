import numpy as np
import matplotlib.pyplot as plt

a, b = 1.1, np.e
n = 100
E = 1e-10
e = 1
x = np.linspace(a, b, n)
h = (b - a) / n
t = 0
y = np.ndarray(n)
dy_dx = np.ndarray(n)
dy_dt = np.ndarray(n)
dy_dt_dx = np.ndarray(n)


while e > E:
    #Задача Коши для y методом Эйлера
    y[0] = a*np.log(a)
    dy_dx[0] = t

    for i in range(n - 1):
        y[i + 1] = y[i] + h * dy_dx[i]
        dy_dx[i + 1] = dy_dx[i] + \
            + h * np.sqrt(1 / x[i]**2 - np.exp(dy_dx[i]) * y[i] + np.e / np.log(x[i]) * y[i]**2)

    #Задача Коши для dy/dt методом Эйлера
    dy_dt[0] = 0
    dy_dt_dx[0] = 1

    for i in range(n - 1):
        dy_dt[i + 1] = dy_dt[i] + h * dy_dt_dx[i]
        dy_dt_dx[i + 1] = dy_dt_dx[i] + h * ((-np.exp(dy_dx[i]) + 2 * np.e * y[i] / np.log(x[i])) / 2 \
            / np.sqrt(1 / x[i]**2 - np.exp(dy_dx[i]) * y[i] + np.e / np.log(x[i]) * y[i]**2) * dy_dt[i] \
                - y[i] * np.exp(dy_dx[i]) / 2 / np.sqrt(1 / x[i]**2 - np.exp(dy_dx[i]) * y[i] + np.e / np.log(x[i]) * y[i]**2) * dy_dt_dx[i])
    
    T = t
    t -= (y[n - 1] - np.e) / dy_dt[n - 1]
    e = abs(T - t)
    print(t)


y[0] = a*np.log(a)
dy_dx[0] = t

for i in range(n - 1):
    y[i + 1] = y[i] + h * dy_dx[i]
    dy_dx[i + 1] = dy_dx[i] + \
        + h * np.sqrt(1 / x[i]**2 - np.exp(dy_dx[i]) * y[i] + np.e / np.log(x[i]) * y[i]**2)

print(y[n - 1])
plt.plot(x, y)
plt.show()