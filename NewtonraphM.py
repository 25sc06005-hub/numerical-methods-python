def newton_raphson(x, f, df, tol):
    while abs(f(x)) > tol:
        x = x - f(x) / df(x)
    return x