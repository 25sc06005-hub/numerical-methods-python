def simpson_38(a, b, f, n):
    h = (b - a) / n
    sum1 = 0
    sum2 = 0

    for i in range(1, n):
        if i % 3 == 0:
            sum2 += f(a + i * h)
        else:
            sum1 += f(a + i * h)

    return (3 * h / 8) * (f(a) + f(b) + 3 * sum1 + 2 * sum2)