import numpy as np

def f(x):
    return x * np.exp(-x**2)

e = 1e-6
x_max = 2**(-1/2)
f_max = f(x_max)

x = 0
while abs(f(x) - f_max / 2) > e:
    x = f_max / 2 * np.exp(x**2)
x_l = x

x = 1
while abs(f(x) - f_max / 2) > e:
    x = (np.log(2 * x / f_max))**(1/2)
x_r = x

print("left " + str(x_l))
print("right " + str(x_r))

print(x_r - x_l)