def simpson_13(a, b, f, n):
    h = (b - a) / n
    sum1 = 0
    sum2 = 0

    for i in range(1, n, 2):
        sum1 += f(a + i * h)

    for i in range(2, n - 1, 2):
        sum2 += f(a + i * h)

    return (h / 3) * (f(a) + f(b) + 4 * sum1 + 2 * sum2)