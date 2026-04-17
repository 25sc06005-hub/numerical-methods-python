import numpy as np
import matplotlib.pyplot as plt

def lagrange_vec(x, y, t):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    val = 0
    for i in range(n):
        # Create a list of all x values except the current x[i]
        others = np.delete(x, i)
        # Calculate the basis polynomial L_i(t) in one line
        L = np.prod((t - others) / (x[i] - others))
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