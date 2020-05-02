import matplotlib.pyplot as plt
import numpy as np

x = [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]
y = [92228496, 106021537, 123202624, 132164569, 151325798, 179323175, 203211926, 226545805, 248709873, 281421906]

class NewtonPol:
    def __init__(self, x, y):
        self.x = np.copy(x)
        self.y = np.copy(y)
        self.pol_length = len(x)
        self.c = np.array(y, dtype=np.float64)

        for j in range(1, self.pol_length):
            for i in range(self.pol_length - 1, j - 1, -1):
                self.c[i] = (self.c[i - 1] - self.c[i]) / (self.x[i - j] - self.x[i])

    def inX(self, x):
        p = 0
        for i in range(self.pol_length):
            m = 1
            for j in range(i):
                m *= x - self.x[j]
            p += self.c[i] * m
        return p


class CubicSpline:
    def __init__(self, x, y):
        self.x = np.copy(x)
        self.y = np.copy(y)
        self.h = x[1] - x[0]
        self.knots = len(x)
        self.a = self.y
        self.c = np.ndarray(self.knots)
        self.d = np.ndarray(self.knots - 1)
        self.b = np.ndarray(self.knots - 1)

        f = np.array(y, dtype=np.float64)
        p = np.ndarray(self.knots - 3)
        q = np.ndarray(self.knots - 3)

        for j in range(1, 3):
            for i in range(self.knots - 1, j - 1, -1):
                f[i] = (f[i - 1] - f[i]) / (x[i - j] - x[i])
        f = 6 * np.delete(f, [0, 1])
        
        p[0] = -1/4
        q[0] = f[0] / 2
        for i in range(1, self.knots - 3):
            p[i] = -1/2 / (p[i - 1] / 2 + 2)
            q[i] = (f[i] - q[i - 1] / 2) / (p[i - 1] / 2 + 2)

        self.c[0] = 0
        self.c[self.knots - 1] = 0
        self.c[self.knots - 2] = (f[self.knots - 3] - q[self.knots - 4] / 2) / (p[self.knots - 4] / 2 + 2)
        for i in range(self.knots - 3, 0, -1):
            self.c[i] = self.c[i + 1] * p[i - 1] + q[i -1]

        for i in range(self.knots - 1):
            self.d[i] = (self.c[i + 1] - self.c[i]) / self.h

        for i in range(self.knots - 1):
            self.b[i] = (self.a[i + 1] - self.a[i]) / self.h + (2 * self.c[i + 1] + self.c[i]) / 6 * self.h

    def inX(self, x0):
        if x0 >= x[self.knots - 1]:
            index = self.knots - 1
        else:
            index = x.index(min(filter(lambda k: k > x0, x)))
        s = self.a[index] + self.b[index - 1] * (x0 - self.x[index]) + \
            self.c[index] / 2 * (x0 - self.x[index])**2 + \
            self.d[index - 1] / 6 * (x0 - self.x[index])**3
        return s


npol = NewtonPol(x, y)
spline = CubicSpline(x, y)
test = np.linspace(x[0] - 15, x[len(x) - 1] + 8, 500)
plt.plot(x, y, 'o', test, list(map(spline.inX, test)), test, list(map(npol.inX, test)), '--')
plt.show()

print(int(npol.inX(2010)))   #308 745 538
print(int(spline.inX(2010)))