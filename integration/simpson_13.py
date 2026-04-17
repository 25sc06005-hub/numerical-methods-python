def simpson_13(a, b, f, n):
    if n % 2 != 0:
        raise ValueError("n must be even")

    h = (b - a) / n
    sum1 = 0
    sum2 = 0

    for i in range(1, n, 2):
        sum1 += f(a + i * h)

    for i in range(2, n, 2):
        sum2 += f(a + i * h)

    return (h / 3) * (f(a) + f(b) + 4 * sum1 + 2 * sum2)


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    f = lambda x: x**2

    a, b = 0, 2
    n = 4  # ✅ must be even

    # Dense curve (actual function)
    x_dense = np.linspace(a, b, 100)
    y_dense = f(x_dense)

    # Sample points
    x_pts = np.linspace(a, b, n+1)
    y_pts = f(x_pts)

    # Plot
    plt.plot(x_dense, y_dense, label="f(x)")
    plt.scatter(x_pts, y_pts, label="Sample Points")

    plt.title("Simpson 1/3 Rule (Corrected)")
    plt.legend()
    plt.grid()

    print("Approx Integral:", simpson_13(a, b, f, n))

    plt.show()