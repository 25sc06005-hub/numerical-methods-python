def divided_diff_table(x, y):
    n = len(x)
    # Explicitly set float type for precision
    D = np.zeros((n, n), dtype=float)
    D[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            # i+j is the 'far' x-coordinate for the current difference order
            D[i][j] = (D[i + 1][j - 1] - D[i][j - 1]) / (x[i + j] - x[i])
    return D
