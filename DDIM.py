def newton_divided(x, y, t):
    n = len(x)
    D = divided_diff_table(x, y)

    val = D[0][0]
    prod = 1

    for i in range(1, n):
        prod *= (t - x[i - 1])
        val += D[0][i] * prod

    return val