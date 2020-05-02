import numpy as np
import matplotlib.pyplot as plt

a = 1 / 2

h = 0.05
Ku = 0.5
t = h * Ku / a
N = int(10 / h)
M = 500

x = np.linspace(0, 10, N)
u = np.zeros((N, M))

u[x < 1, 0] = 0
u[x >= 1, 0] = x[x >= 1] - 1
u[x >= 2, 0] = 3 - x[x >= 2]
u[x >= 3] = 0

# print(u[:, 0])

for j in range(M - 1):
    for i in range(2, N + 2):
        if (i == N):
            u[0, j + 1] = u[0, j] - Ku * (u[N - 2, j] - 4 * u[N - 1, j] + 3 * u[0, j]) / 2 + \
                Ku**2 * (u[N - 2, j] - 2 * u[N - 1, j] + u[0, j]) / 2
        elif (i == N + 1):
            u[1, j + 1] = u[1, j] - Ku * (u[N - 1, j] - 4 * u[0, j] + 3 * u[1, j]) / 2 + \
                Ku**2 * (u[N - 1, j] - 2 * u[0, j] + u[1, j]) / 2
        else:
            u[i, j + 1] = u[i, j] - Ku * (u[i - 2, j] - 4 * u[i - 1, j] + 3 * u[i, j]) / 2 + \
                Ku**2 * (u[i - 2, j] - 2 * u[i - 1, j] + u[i, j]) / 2

plt.plot(x, u[:, 0], x, u[:, M - 1], x, u[:, int(M / 2)])
plt.show()