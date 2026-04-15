def newton_backward(x, y, t):
    n = len(x)
    h = x[1] - x[0]
    D = diff_table(y)
    p = (t - x[-1]) / h

    val = y[-1]
    fact = 1
    pterm = 1

    for i in range(1, n):
        pterm *= (p + (i - 1))
        fact *= i
        val += (pterm * D[n - i - 1][i]) / fact

    return val