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

my = NewtonPol(x, y)
print(my.inX(2010))   #308 745 538


#print("f'(1950) = " + str((y[5]-y[4])/10))