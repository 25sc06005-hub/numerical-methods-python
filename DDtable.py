def divided_diff_table(x, y):
    n = len(x)
    D = np.zeros((n, n))
    D[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            D[i][j] = (D[i + 1][j - 1] - D[i][j - 1]) / (x[i + j] - x[i])

    return D