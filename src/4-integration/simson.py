import sys

sys.path.append('../../libs/')
from functiontools import function
from integralutil import get_interval_points

def simson(dx, fs):

    integral = 0.0
    for i in range(n):
        integral += fs[2*i] + 4*fs[2*i+1] + fs[2*i+2]

    integral *= dx/6
    return integral

if __name__ == "__main__":
    n = int(input("Enter n: "))
    intLimits = [float(x) for x in input("Please enter integration limits: ").split(' ')]
    expr = input("Please give the function to be integrated: ")

    f = function(expr)

    # Simson rule requires that interval is separated in 2*n equal intervals
    dx, y = get_interval_points(2*n + 1, f, intLimits)
    
    print(simson(2*dx, y))