def trapezoidal(a, b, f, n):
    h = (b - a) / n
    total = 0

    for i in range(1, n):
        total += f(a + i * h)

    return (h / 2) * (f(a) + f(b) + 2 * total)


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    f = lambda x: x**2

    a, b = 0, 2
    n = 4
    h = (b - a) / n

    x = np.linspace(a, b, n+1)
    y = f(x)

    plt.plot(x, y)
    plt.fill_between(x, y, step='mid', alpha=0.3)

    plt.title("Trapezoidal Rule")
    plt.grid()
    plt.show()