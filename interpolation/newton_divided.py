import numpy as np
import matplotlib.pyplot as plt

def divided_diff_table(x, y):
    n = len(x)
    # Create a table and initialize the first column with y
    D = np.zeros((n, n))
    D[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            # Formula: (f[x_{i+1}...x_j] - f[x_i...x_{j-1}]) / (x_{i+j} - x_i)
            D[i][j] = (D[i+1][j-1] - D[i][j-1]) / (x[i+j] - x[i])
    return D

def newton_divided(x, y, t):
    n = len(x)
    D = divided_diff_table(x, y)

    # val starts with f[x0]
    val = D[0][0]
    prod = 1

    for i in range(1, n):
        # Multiply by (t - x_{i-1})
        prod *= (t - x[i-1])
        # Use coefficients from the top row of the divided difference table
        val += D[0][i] * prod

    return val

if __name__ == "__main__":
    # Example data (Unequally spaced to demonstrate divided difference utility)
    x_data = np.array([0, 1, 2, 5])
    y_data = np.array([1, 3, 2, 10])

    # Generate points for a smooth curve
    x_plot = np.linspace(min(x_data), max(x_data), 100)
    y_plot = [newton_divided(x_data, y_data, t) for t in x_plot]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_plot, label="Newton Divided Diff Interpolation", color='purple', linewidth=2)
    plt.scatter(x_data, y_data, color='red', s=50, zorder=5, label="Data Points")

    plt.title("Newton's Divided Difference Interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
