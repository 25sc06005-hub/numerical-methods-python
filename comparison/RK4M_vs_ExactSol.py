

def rk4(x0, y0, f, h, n):
    x = [x0]
    y = [y0]

    for i in range(n):
        k1 = h * f(x[-1], y[-1])
        k2 = h * f(x[-1]+h/2, y[-1]+k1/2)
        k3 = h * f(x[-1]+h/2, y[-1]+k2/2)
        k4 = h * f(x[-1]+h, y[-1]+k3)

        y.append(y[-1] + (k1+2*k2+2*k3+k4)/6)
        x.append(x[-1] + h)

    return x, y


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    f = lambda x, y: x + y
    exact = lambda x: np.exp(x) - x - 1

    x_rk, y_rk = rk4(0, 1, f, 0.1, 20)

    x_vals = np.linspace(0, 2, 100)

    plt.plot(x_vals, exact(x_vals), label="Exact")
    plt.plot(x_rk, y_rk, marker='o', label="RK4")

    plt.legend()
    plt.title("RK4 vs Exact Solution")
    plt.grid()
    plt.show()