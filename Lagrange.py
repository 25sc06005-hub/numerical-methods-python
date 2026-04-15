def lagrange(x, y, t):
    n = len(x)
    val = 0

    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (t - x[j]) / (x[i] - x[j])
        val += y[i] * L

    return val