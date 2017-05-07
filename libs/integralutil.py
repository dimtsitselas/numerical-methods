from functiontools import function
from sympy.solvers import solve
from math import inf


def get_interval_points(n, func, interval):
    """
    Method to separate an interval to equal intervals and get the value of a
    function of their leftmost points

    n:
        number of intervals that interval will be separated
    
    func:
        the function we are interested in. Func is an instance of fuction class 
        that is implemented in functiontools.py
    interval:
        interval is a list, i.e. [2,5.4] that specifies the interval in the x axis 
        that will be separated in n equal integrals

    ex. if we have the interval [1,3] and n = 2 then xs = [1,2,3]
    and if func = 2x + 1, fs = [3, 5, 7]
    """
    if len(interval) != 2:
        raise ValueError("interval must have only two elements, i.e. [3, 3.5]")
    a, b = interval[:]
    if(b < a):
        a, b = b, a
    elif a == b:
        raise ValueError("An interval must consist of two different numbers")
    
    dx = (b - a)/float(n)

    # xs contains the points on which we separate the interval
    # and fs the value of f at these points
    xs = [a + i * dx for i in range(n + 1)]
    fs = [func(x) for x in xs]

    return dx, fs


def funcMax(func, interval):
    """
    Function that returns the maximum of a function in an interval

    func:
        The function whose the maximum we are searching for. Fucntion is an insance
        of function class that is implemented in functiontools.py
    interval:
        The interval in which we want to find the maximum
        Interval should be a list of two floats
    """

    if len(interval) != 2:
        raise ValueError("interval must have only two elements, i.e. [3, 3.5]")
    a, b = interval[:]
    if(b < a):
        a, b = b, a
    elif a == b:
        raise ValueError("An interval must consist of two different numbers")

    # First and second derivatives of func
    firstder = func.diff()
    if firstder.isConstant():
        # Func is a first degree polynomial and its derivative is constant
        # Sympy can't handle devitives of a constant function. If func has
        # a positive slope then we should return func(b), else we should
        # return func(a)
        return max(func(a), func(b))
    secondder = func.diff(2)

    """
    To find the global maximum of func in interval we first solve df/dx = 0
    Then we check if the second derivative is negative on these points, which
    is the condition for checking for local maximum. Of these local maxima
    and the values of func at a and b we want the one that is bigger
    """
    solutionsExpr = solve(firstder)
    solutions = list(map(lambda x: x.evalf(), solutionsExpr))

    maxOfFunc = max(func(a), func(b))
    for point in solutions:
        if secondder(point) < 0:
            # we have a local maximum
            maxOfFunc = max(func(point), maxOfFunc)
    
    return maxOfFunc

if __name__ == "__main__":
    expr = input("Enter a function: ")
    f = function(expr)
    
    print(funcMax(f, [-10, 10]))