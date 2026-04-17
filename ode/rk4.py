def rk4_system(x0, y0, f, h, n):
    # y0 can be a list or array [y1, y2, ...]
    y = np.array(y0)
    x = x0
    results_x = [x]
    results_y = [y]

    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        
        results_x.append(x)
        results_y.append(y)

    return np.array(results_x), np.array(results_y)



if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    # dy/dx = x + y
    f = lambda x, y: x + y

    x, y = rk4(0, 1, f, 0.1, 20)

    plt.plot(x, y, marker='o')
    plt.title("RK4 Solution of dy/dx = x + y")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()

    plt.show()