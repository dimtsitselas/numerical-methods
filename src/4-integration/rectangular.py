import sys

sys.path.append('../../libs/')
from functiontools import function
from integralutil import *

def rectangular(dx, fs):

    integral = 0.0
    for y in fs:
        integral+=y
    
    integral *= dx
    return integral

def err(func, dx, interval):
    
    a, b = interval[:]
    return dx/2 * (b - a) * funcMax(func.diff(), interval)


if __name__ == "__main__":
    n = int(input("Enter n: "))
    intLimits = [float(x) for x in input("Please enter integration limits: ").split(' ')]
    expr = input("Please give the function to be integrated: ")

    f = function(expr)

    dx, y = get_interval_points(n - 1, f, intLimits)
    

    print(rectangular(dx, y))
    print("Biggest error of the above intergation has absolute value of: " + str(err(f, dx, intLimits)))