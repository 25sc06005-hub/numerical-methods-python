
def bisection(a, b, f, tol):
    points = []

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        points.append(c)

        if f(c) == 0:
            return c, points
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2, points




if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

        
    # Function
    f = lambda x: x**3 - x - 2

    # Run method
    root, points = bisection(1, 2, f, 0.001)

    # Plot function
    x_vals = np.linspace(0, 3, 100)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0)

    # Plot iterations
    plt.scatter(points, [f(p) for p in points], label="Iterations")

    plt.title("Bisection Method Visualization")
    plt.legend()
    plt.grid()

    plt.show()
