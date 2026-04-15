import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**2

x = np.linspace(0, 2, 100)
y = f(x)

plt.plot(x, y)

x_pts = np.linspace(0, 2, 5)
plt.scatter(x_pts, f(x_pts))

plt.title("Simpson's 1/3 Rule")
plt.grid()
plt.show()