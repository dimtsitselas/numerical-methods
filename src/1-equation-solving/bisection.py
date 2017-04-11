import sys

sys.path.append('../../libs/')
from functiontools import function

def bisection(expr, lo, hi, tolerance=0.001):
    f = function(expr)

    k = 1
    while abs(hi - lo) >= tolerance:
        medium = (hi + lo)/2

        if f(lo) * f(medium) <= 0:
            hi = medium
        else:
            lo = medium
        
        k += 1

    return k, lo, hi

def main(args):

    if len(args) < 4:
        raise AttributeError("Too few arguments")
    
    elif len(args) == 4:
        expr, left, right = args[1:4]
        n, lo, hi = bisection(expr, float(left), float(right))

    elif len(sys.args) == 5:
        tolerance = float(sys.argv[4])
        n, lo, hi = bisection(epxr, float(left), float(right), float(tolerance))

    else:
        raise AttributeError("Too many arguments")

    print ("After " + str(n) + " iterations, a solution was found in the interval (" + str(lo) + ", " + str(hi) + ")")

if __name__ == '__main__':
    main(sys.argv)