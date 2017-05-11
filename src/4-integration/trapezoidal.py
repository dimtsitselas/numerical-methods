import sys

sys.path.append('../../libs/')
from functiontools import function
from integralutil import *

"""def trapezodial(dx, fs):

    integral = 0.0
    for i in range(0, n):
        integral += fs[i] + fs[i+1]
    
    integral *= dx/2
    return integral"""

def trapezodial(expr, interval, N):
    func = function(expr)
    dx, fs = getIntervalPoints(N , func, interval)

    integral = 0.0
    for i in range(N):
        integral += fs[i] + fs[i+1]
    integral *= dx/2

    return integral, maxErr(func, dx, interval)

def maxErr(func, dx, interval):
    a, b = interval[:]
    
    return dx**2/12 * (b - a) * funcMax(func.diff(2), interval)

if __name__ == "__main__":
    expr = input("Please give the function to be integrated: ")
    intLimits = [float(x) for x in input("Please enter integration limits: ").split(' ')]    
    n = int(input("Enter n: "))    

    I, error = trapezodial(expr, intLimits, n)

    print("Integral is: " + str(I))
    print("Max error of the above intergation has absolute value of: " + str(error))
