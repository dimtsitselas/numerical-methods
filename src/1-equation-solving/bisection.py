import sys
sys.path.append('/home/toliz/Desktop/GitHub/numerical-methods/libs/')

from functiontools import function

def bisection(expr, lo, hi, tolerance=0.001):
    f = function(expr)

    k = 1
    while abs(hi - lo) >= tolerance:
        medium = (hi + lo)/2
        if f.eval(lo) * f.eval(medium) <= 0:
            hi = medium
        else:
            lo = medium
        k = k + 1

    return k, lo, hi

def main(args):

    if len(args) < 4:
        raise AttributeError("Too few arguments")
    
    elif len(args) == 4:
        expr, left, right = args[1:4]
        n, lo, hi = bisection(expr, int(left), int(right))

    elif len(sys.args) == 5:
        tolerance = float(sys.argv[4])
        n, lo, hi = bisection(epxr, int(left), int(right), int(tolerance))

    else:
        raise AttributeError("Too many arguments")

    print ("After " + str(n) + " iterations, a solution was found in the interval (" + str(lo) + ", " + str(hi) + ")")

if __name__ == '__main__':
    main(sys.argv)