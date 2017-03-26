import time
import sys

def evaluate(point):
    return 3*point + 2

def bisection(lo, hi, tolerance=0.003):
    k = 1
    while abs(hi - lo) >= tolerance:
        medium = (hi + lo)/2
        if evaluate(lo) * evaluate(medium) <= 0:
            hi = medium
        else:
            lo = medium
        k = k + 1

    return k, lo, hi

def main():
    left, right = list(map(int, sys.argv[1:3]))
    if len(sys.argv) == 4:
        tolerance = float(sys.argv[-1])
        n, lo, hi = bisection(left, right, tolerance)
    else:
        n, lo, hi = bisection(left, right)
    print ("After " + str(n) + " iterations, a solution was found in the interval (" + str(lo) + ", " + str(hi) + ")")

if __name__ == '__main__':
    main()
