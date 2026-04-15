import matplotlib.pyplot as plt

def rk4(x0, y0, f, h, n):
    x = [x0]
    y = [y0]

    for i in range(n):
        k1 = h * f(x[-1], y[-1])
        k2 = h * f(x[-1] + h/2, y[-1] + k1/2)
        k3 = h * f(x[-1] + h/2, y[-1] + k2/2)
        k4 = h * f(x[-1] + h, y[-1] + k3)

        y_next = y[-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_next = x[-1] + h

        x.append(x_next)
        y.append(y_next)

    return x, y


# dy/dx = x + y
f = lambda x, y: x + y

x, y = rk4(0, 1, f, 0.1, 20)

plt.plot(x, y, marker='o')
plt.title("RK4 Solution of dy/dx = x + y")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

plt.show()