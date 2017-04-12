import sys

sys.path.append('../../libs/')
from functiontools import function

def fixed_point(expr, point=0, tolerance=0.001):
    """Uses fixed point method to solve the equation: expr = 0"""
    
    # TODO: implement Aitken acceleration    
    f = function(expr + "+x")

    k, maxiter = 0, 1000
    while True:
        k += 1
        newPoint = f(point)

        if abs(newPoint - point) < tolerance:
            break
        elif k > maxiter:
            return Exception("Failed to convert in %d iterations" % maxiter)
        else:
            point = newPoint
        
    return point, k # (solution, iterations)

def main(args):
    
    if len(args) < 3:
        raise AttributeError("Too few arguments")
    
    elif len(args) == 3:
        expr, point = args[1:]
        try:
            sol, n = fixed_point(expr, float(point))
        except Exception as e:
            print ("Failed to converge in 1000 iterations")
            return -1

    elif len(sys.args) == 4:
        expr, point, tolerance = args[1:]
        try:
            sol, n = fixed_point(epxr, float(point), float(tolerance))
        except Exception as e:
            print ("Failed to converge in 1000 iterations")
            return -1

    else:
        raise AttributeError("Too many arguments")

    print ("After " + str(n) + " iterations, a solution is approximately " + str(sol))

if __name__ == '__main__':
    main(sys.argv)
