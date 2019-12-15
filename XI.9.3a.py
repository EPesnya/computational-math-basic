import numpy as np
import matplotlib.pyplot as plt

a, b = 0, 1
n = 100
E = 1e-6
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
    y[0] = 0
    dy_dx[0] = t

    for i in range(n - 1):
        y[i + 1] = y[i] + h * dy_dx[i]
        dy_dx[i + 1] = dy_dx[i] + h * x[i] * np.sqrt(y[i])

    #Задача Коши для dy/dt методом Эйлера
    dy_dt[0] = 0
    dy_dt_dx[0] = 1

    for i in range(n - 1):
        dy_dt[i + 1] = dy_dt[i] + h * dy_dt_dx[i]
        dy_dt_dx[i + 1] = dy_dt_dx[i] + h * x[i] / 2 / np.sqrt(y[i]) * dy_dt[i]
    
    T = t
    t -= (y[n - 1] - 2) / dy_dt[n - 1]
    e = abs(T - t)
    print(t)


y[0] = 0
dy_dx[0] = t

for i in range(n - 1):
    y[i + 1] = y[i] + h * dy_dx[i]
    dy_dx[i + 1] = dy_dx[i] + h * x[i] * np.sqrt(y[i])

plt.plot(x, y)
plt.show()