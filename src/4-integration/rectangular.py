import sys

sys.path.append('../../libs/')
from functiontools import function
from integralutil import *

def rectangular(expr, interval, N):
    func = function(expr)
    dx, fs = getIntervalPoints(N, func, interval)
    
    # Integral computation
    integral = 0.0
    for i in range(N):
        integral += fs[i] 
    integral *= dx

    return integral, maxErr(func, dx, interval)

def maxErr(func, dx, interval):
    a, b = interval[:]

    return dx / 2 * (b - a) * abs(funcMax(func.diff(), interval))

if __name__ == "__main__":
    
    expr = input("Please give the function to be integrated: ")
    intLimits = [float(x) for x in input("Please enter integration limits: ").split(' ')]    
    n = int(input("Enter n: "))    

    I, error = rectangular(expr, intLimits, n)

    print("Integral is: " + str(I))
    print("Max error of the above intergation has absolute value of: " + str(error))
