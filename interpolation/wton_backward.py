import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def diff_table(y):
    n = len(y)
    D = np.zeros((n, n))
    D[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            D[i][j] = D[i + 1][j - 1] - D[i][j - 1]
    return D

def newton_backward(x, y, t):
    n = len(x)
    h = x[1] - x[0]
    D = diff_table(y)
    p = (t - x[-1]) / h

    val = D[n-1][0] # Starting with y_n
    pterm = 1
    
    for i in range(1, n):
        pterm *= (p + (i - 1))
        # In a forward table, the backward difference Nabla^i y_n 
        # is found at index [n-i-1][i]
        val += (pterm * D[n - i - 1][i]) / factorial(i)

    return val

if __name__ == "__main__":
    # Test Data: Powers of 2
    x = np.array([0, 1, 2, 3])
    y = np.array([1, 2, 4, 8])

    x_vals = np.linspace(0, 3, 100)
    y_vals = [newton_backward(x, y, t) for t in x_vals]

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="Newton Backward Path", color='blue', linewidth=2)
    plt.scatter(x, y, color='red', zorder=5, label="Data Points")

    plt.title("Newton Backward Interpolation (Python)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
