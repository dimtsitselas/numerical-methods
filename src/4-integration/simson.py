import sys

sys.path.append('../../libs/')
from functiontools import function
from integralutil import *

def simpson(expr, interval, N):
    func = function(expr)
    # Simpson rule requires that interval is separated in 2*n equal intervals
    dx, fs = getIntervalPoints(2*N, func, interval) 
    dx *= 2 # dx must be (b-a)/6 not (b-a)/12

    integral = 0.0
    for i in range(N):
        integral += fs[2*i] + 4*fs[2*i+1] + fs[2*i+2]
    integral *= dx/6

    return integral, maxErr(func, dx, interval)

def maxErr(func, dx, interval):
    a, b = interval[:]

    return (dx/2)**4/180 * (b - a) * funcMax(func.diff(4), interval)

if __name__ == "__main__":
    expr = input("Please give the function to be integrated: ")
    intLimits = [float(x) for x in input("Please enter integration limits: ").split(' ')]    
    n = int(input("Enter n: "))    

    I, error = simpson(expr, intLimits, n)

    print("Integral is: " + str(I))
    print("Max error of the above intergation has absolute value of: " + str(error))
