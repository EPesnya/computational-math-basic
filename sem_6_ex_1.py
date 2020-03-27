import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

T = 18
L = 20
h = 0.5
Ku = 0.6
t = h * Ku

def function_t0(x):
    return np.sin(4 * np.pi * x / L)

N = int(L / h) + 1
x = np.linspace(0, L, N)

def solve1(Ku, t):
    M = int(T / t) + 1

    u = np.zeros((M, N))

    u[0] = function_t0(x)

    for j in range(M - 1):
        for i in range(1, N):
            u[j + 1, i] = u[j, i] - t * (u[j, i] - u[j, i - 1]) / h
        u[j + 1, 0] = u[j + 1, N - 1]

    return u


def solve2(Ku, t):
    M = int(T / t) + 1

    u = np.zeros((M, N))

    u[0] = function_t0(x)

    for j in range(M - 1):
        for i in range(1, N - 1):
            u[j + 1, i] = u[j, i] - t * (u[j, i + 1] - u[j, i - 1]) / 2 / h + \
                + t**2 / 2 * (u[j, i + 1] - 2 * u[j, i] + u[j, i - 1]) / h**2
        u[j + 1, N - 1] = u[j, N - 1] - t * (u[j, 0] - u[j, N - 2]) / 2 / h + \
            + t**2 / 2 * (u[j, 0] - 2 * u[j, N - 1] + u[j, N - 2]) / h**2
        u[j + 1, 0] = u[j + 1, N - 1]

    return u


################

def print_solve(method, text):
    u = method(Ku, t)

    fig, ax = plt.subplots()
    fig.suptitle(text)
    plt.subplots_adjust(bottom=0.3)
    l = ax.plot(x, u[0, :], x, function_t0(x), lw=2)
    ax.margins(x=0)

    axtime = plt.axes([0.35, 0.1, 0.5, 0.03])
    stime = Slider(axtime, 'T:', 0.0, T, valfmt='%d', valstep=1)

    def update(val):
        time = int(stime.val / t)
        l[0].set_ydata(u[time, :])
        l[1].set_ydata(function_t0(x - stime.val))
        fig.canvas.draw_idle()

    stime.on_changed(update)


    rax = plt.axes([0.12, 0.05, 0.15, 0.15])
    radio = RadioButtons(rax, (0.6, 1, 1.1), active=0)

    def colorfunc(label):
        Ku = float(label)
        t = h * Ku
        u = method(Ku, t)
        time = int(stime.val / t)
        l[0].set_ydata(u[time, :])
        l[1].set_ydata(function_t0(x - stime.val))

        def update(val):
            time = int(stime.val / t)
            l[0].set_ydata(u[time, :])
            l[1].set_ydata(function_t0(x - stime.val))
            fig.canvas.draw_idle()

        stime.on_changed(update)

        fig.canvas.draw_idle()

    radio.on_clicked(colorfunc)

    plt.show()



print_solve(solve1, 'Схема уголок')
print_solve(solve2, 'Схема Лакса-Вендрофа')
