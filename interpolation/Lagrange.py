import numpy as np
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]

    x_vals = np.linspace(1, 4, 100)
    y_vals = [lagrange(x, y, t) for t in x_vals]

    plt.plot(x_vals, y_vals, label="Interpolated Curve")
    plt.scatter(x, y, color='red', label="Data Points")

    plt.title("Lagrange Interpolation")
    plt.legend()
    plt.grid()

    print("Value at t=2.5:", lagrange(x, y, 2.5))

    plt.show()