import numpy as np
import matplotlib.pyplot as plt

from math import factorial

def diff_table(y):
    n = len(y)
    D = np.zeros((n, n))
    D[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            D[i][j] = D[i+1][j-1] - D[i][j-1]
    return D

def newton_forward(x, y, t):
    n = len(x)
    h = x[1] - x[0]
    D = diff_table(y)
    p = (t - x[0]) / h

    val = y[0]
    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (p - j)
        val += (term * D[0][i]) / factorial(i)
    return val

x = [0, 1, 2, 3]
y = [1, 2, 4, 8]

x_vals = np.linspace(0, 3, 100)
y_vals = [newton_forward(x, y, t) for t in x_vals]

plt.plot(x_vals, y_vals)
plt.scatter(x, y)

plt.title("Newton Forward Interpolation")
plt.grid()
plt.show()