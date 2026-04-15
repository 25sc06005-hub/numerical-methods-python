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