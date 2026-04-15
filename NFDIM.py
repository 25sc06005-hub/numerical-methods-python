def newton_forward(x, y, t):
    n = len(x)
    h = x[1] - x[0]
    D = diff_table(y)
    p = (t - x[0]) / h

    val = y[0]
    fact = 1
    pterm = 1

    for i in range(1, n):
        pterm *= (p - (i - 1))
        fact *= i
        val += (pterm * D[0][i]) / fact

    return val