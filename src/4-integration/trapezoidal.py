import sys

sys.path.append('../../libs/')
from functiontools import function
from integralutil import *

def trapezodial(dx, fs):

    integral = 0.0
    for i in range(0, n):
        integral += fs[i] + fs[i+1]
    
    integral *= dx/2
    return integral

def err(func, dx, interval):

    a, b = interval[:]
    return dx**2/12 * (b - a) * funcMax(func.diff(2), interval)

if __name__ == "__main__":
    n = int(input("Enter n: "))
    intLimits = [float(x) for x in input("Please enter integration limits: ").split(' ')]
    expr = input("Please give the function to be integrated: ")

    f = function(expr)

    dx, y = get_interval_points(n , f, intLimits)

    print("Calculating ...\n" + str(trapezodial(dx, y)))
    print("Biggest error of the above intergation has absolute value of: " + str(err(f, dx, intLimits)))