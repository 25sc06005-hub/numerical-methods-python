def simpson_38(a, b, f, n):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3")

    h = (b - a) / n
    sum1 = 0
    sum2 = 0

    for i in range(1, n):
        if i % 3 == 0:
            sum2 += f(a + i * h)
        else:
            sum1 += f(a + i * h)

    return (3 * h / 8) * (f(a) + f(b) + 3 * sum1 + 2 * sum2)


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    f = lambda x: x**2

    a, b = 0, 2
    n = 6   

    x_dense = np.linspace(a, b, 100)
    y_dense = f(x_dense)

    x_pts = np.linspace(a, b, n+1)
    y_pts = f(x_pts)

    plt.plot(x_dense, y_dense, label="f(x)")
    plt.scatter(x_pts, y_pts, label="Sample Points")

    plt.title("Simpson 3/8 Rule (Corrected)")
    plt.legend()
    plt.grid()
    plt.show()