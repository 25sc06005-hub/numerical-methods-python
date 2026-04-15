import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# -------- Lagrange --------
def lagrange(x, y, t):
    n = len(x)
    val = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (t - x[j]) / (x[i] - x[j])
        val += y[i] * L
    return val


# -------- Newton Forward --------
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


# -------- Main --------
if __name__ == "__main__":
    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]

    x_vals = np.linspace(1, 4, 100)

    y_lagrange = [lagrange(x, y, t) for t in x_vals]
    y_newton = [newton_forward(x, y, t) for t in x_vals]

    # Plot
    plt.plot(x_vals, y_lagrange, label="Lagrange", linestyle='--')
    plt.plot(x_vals, y_newton, label="Newton Forward")
    plt.scatter(x, y, color='red', label="Data Points")

    plt.title("Lagrange vs Newton Forward Interpolation")
    plt.legend()
    plt.grid()

    plt.show()