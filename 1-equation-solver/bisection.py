import time
import sys

def evaluate(point):
    return 3*point + 2

def bisection(lo, hi):
    eps = 1e-08
    k = 1
    while abs(hi - lo) >= eps:
        medium = (hi + lo)/2
        if evaluate(lo) * evaluate(medium) <= 0:
            hi = medium
        else:
            lo = medium
        k = k + 1

    return k, lo, hi

if __name__ == '__main__':
    left, right = list(map(int, sys.argv[1:3]))
    print(bisection(left, right))
