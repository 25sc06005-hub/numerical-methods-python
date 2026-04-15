def diff_table(y):
    n = len(y)
    import numpy as np
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

    val = y[-1]
    fact = 1
    pterm = 1

    for i in range(1, n):
        pterm *= (p + (i - 1))
        fact *= i
        val += (pterm * D[n - i - 1][i]) / fact

    return val


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    x = [0, 1, 2, 3]
    y = [1, 2, 4, 8]

    x_vals = np.linspace(0, 3, 100)
    y_vals = [newton_backward(x, y, t) for t in x_vals]

    plt.plot(x_vals, y_vals, label="Interpolated Curve")
    plt.scatter(x, y, color='red', label="Data Points")

    plt.title("Newton Backward Interpolation")  # ✅ fixed
    plt.legend()
    plt.grid()

    plt.show()