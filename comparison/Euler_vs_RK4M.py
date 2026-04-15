import matplotlib.pyplot as plt

# Euler
def euler(x0, y0, f, h, n):
    x = [x0]
    y = [y0]
    for i in range(n):
        y.append(y[-1] + h * f(x[-1], y[-1]))
        x.append(x[-1] + h)
    return x, y

# RK4 (same as before)

f = lambda x, y: x + y

x1, y1 = euler(0, 1, f, 0.1, 20)
x2, y2 = rk4(0, 1, f, 0.1, 20)

plt.plot(x1, y1, label="Euler")
plt.plot(x2, y2, label="RK4")

plt.legend()
plt.title("Euler vs RK4 Comparison")
plt.grid()

plt.show()