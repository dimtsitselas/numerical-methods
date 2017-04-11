import sys

sys.path.append('../../libs/')
from functiontools import function

def newton_raphson(expr, point=0, tolerance=0.001):
    """Uses newton raphson method to solve the equation: expr = 0"""
    f = function(expr)
    derivative = f.diff()

    k=0
    while True:
        newPoint = point - f(point)/derivative(point)

        k = k + 1
        if abs(newPoint - point) < tolerance:
            break
        else:
            point = newPoint
        
    return point, k  

def main(args):
    
    if len(args) < 3:
        raise AttributeError("Too few arguments")
    
    elif len(args) == 3:
        expr, point = args[1:]
        sol, n = newton_raphson(expr, float(point))

    elif len(sys.args) == 4:
        expr, point, tolerance = args[1:]
        sol, n = newton_raphson(epxr, float(point), float(tolerance))

    else:
        raise AttributeError("Too many arguments")

    print ("After " + str(n) + " iterations, a solution is approximately " + str(sol))

if __name__ == '__main__':
    main(sys.argv)
