def regula_falsi(a, b, f, tol):
    c = a
    while abs(f(c)) > tol:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c



if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

        
    # Function
    f = lambda x: x**3 - x - 2

    # Run method
    root, points = regula_falsi(1, 2, f, 0.001)

    # Plot function
    x_vals = np.linspace(0, 3, 100)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0)

    # Plot iterations
    plt.scatter(points, [f(p) for p in points], label="Iterations")

    plt.title("Regula Falsi Method Visualization")
    plt.legend()
    plt.grid()

    plt.show()