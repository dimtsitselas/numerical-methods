from functiontools import function

def get_interval_points(n, func, interval):
    a, b = interval[:]
    dx = (b - a)/float(n)

    xs = [a + dx for i in range(n)]
    fs = [f(x) for x in xs]

    return xs, fs
