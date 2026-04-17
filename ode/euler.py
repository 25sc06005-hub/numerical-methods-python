def euler(x0, y0, f, h, n):
    x = [x0]
    y = [y0]

    for i in range(n):
        y_next = y[-1] + h * f(x[-1], y[-1])
        x_next = x[-1] + h

        x.append(x_next)
        y.append(y_next)

    return x, y

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    # dy/dx = x + y
    f = lambda x, y: x + y

    x, y = euler(0, 1, f, 0.1, 20)

    plt.plot(x, y, marker='o')
    plt.title("RK4 Solution of dy/dx = x + y")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()

    plt.show()