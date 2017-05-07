from functiontools import function

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
    xs = [a + i * dx for i in range(n)]
    fs = [func(x) for x in xs]

    return dx, fs