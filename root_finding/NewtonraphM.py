
def newton(x, f, df, tol):
    points = [x]

    while abs(f(x)) > tol:
        x = x - f(x)/df(x)
        points.append(x)

    return x, points




if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1

    root, points = newton(1.5, f, df, 0.001)

    x_vals = np.linspace(0, 3, 100)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals)
    plt.axhline(0)
    plt.scatter(points, [f(p) for p in points])

    plt.title("Newton-Raphson Method")
    plt.grid()
    plt.show()