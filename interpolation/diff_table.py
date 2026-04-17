def diff_table(y):
    n = len(y)
    # Use dtype=float to avoid integer division issues in later steps
    D = np.zeros((n, n), dtype=float)
    D[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            # Standard Forward Difference: Delta y_i = y_{i+1} - y_i
            D[i][j] = D[i + 1][j - 1] - D[i][j - 1]
    return D
