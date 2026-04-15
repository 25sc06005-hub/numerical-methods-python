def euler(x0, y0, f, h, n):
    x = [x0]
    y = [y0]

    for i in range(n):
        y_next = y[-1] + h * f(x[-1], y[-1])
        x_next = x[-1] + h

        x.append(x_next)
        y.append(y_next)

    return x, y