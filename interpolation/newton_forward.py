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

    val = D[0][0]  # First y value
    p_product = 1  # To store p(p-1)(p-2)...
    
    for i in range(1, n):
        # Update the product: for i=1 it's (p), for i=2 it's p(p-1), etc.
        p_product *= (p - (i - 1))
        
        # D[0][i] accesses the top row of the table (Forward Differences)
        val += (p_product * D[0][i]) / factorial(i)
        
    return val

if __name__ == "__main__":
    # Test data
    x = np.array([0, 1, 2, 3])
    y = np.array([1, 2, 4, 8])

    x_vals = np.linspace(0, 3, 100)
    y_vals = [newton_forward(x, y, t) for t in x_vals]

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="Interpolated Curve", color='green')
    plt.scatter(x, y, color='red', label="Data Points")
    plt.title("Newton Forward Interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
