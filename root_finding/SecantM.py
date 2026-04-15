import numpy as np
import matplotlib.pyplot as plt

def secant(a, b, f, tol):
    points = [a, b]

    while abs(b - a) > tol:
        c = b - f(b) * (b - a) / (f(b) - f(a))
        points.append(c)
        a, b = b, c

    return b, points

f = lambda x: x**3 - x - 2

root, points = secant(1, 2, f, 0.001)

x_vals = np.linspace(0, 3, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)
plt.axhline(0)
plt.scatter(points, [f(p) for p in points])

plt.title("Secant Method")
plt.grid()
plt.show()