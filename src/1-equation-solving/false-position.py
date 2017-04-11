import sys

sys.path.append('../../libs/')
from functiontools import function

def false_position(expr, lo, hi, tolerance=0.001):
    f = function(expr)

    c, k = 1, 1
    while abs(f(c)) >= tolerance:
        """Uses false position method to solve the equation: expr = 0"""
        c = (lo * f(hi) - hi * f(lo)) / (f(hi) - f(lo))

        if(f(lo) * f(c) <= 0):
            hi = c
        else:
            lo = c

        k += 1

    return k, c

def main(args):
    
    if len(args) < 4:
        raise AttributeError("Too few arguments")
    
    elif len(args) == 4:
        expr, left, right = args[1:4]
        n, sol = false_position(expr, float(left), float(right))

    elif len(sys.args) == 5:
        tolerance = float(sys.argv[4])
        n, sol = false_position(epxr, float(left), float(right), float(tolerance))

    else:
        raise AttributeError("Too many arguments")

    print ("After " + str(n) + " iterations, a solution is approximately " + str(sol))

if __name__ == '__main__':
    main(sys.argv)
