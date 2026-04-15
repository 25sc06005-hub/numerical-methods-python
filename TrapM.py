def trapezoidal(a, b, f, n):
    h = (b - a) / n
    total = 0

    for i in range(1, n):
        total += f(a + i * h)

    return (h / 2) * (f(a) + f(b) + 2 * total)