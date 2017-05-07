import sys

sys.path.append('../../libs/')
from functiontools import function
from integralutil import get_interval_points

def trapezodial(dx, fs):

    integral = 0.0
    for i in range(0, n):
        integral += fs[i] + fs[i+1]
    
    integral *= dx/2
    return integral

if __name__ == "__main__":
    n = int(input("Enter n: "))
    intLimits = [float(x) for x in input("Please enter integration limits: ").split(' ')]
    expr = input("Please give the function to be integrated: ")

    f = function(expr)

    dx, y = get_interval_points(n + 1, f, intLimits)

    print("Calculating ...\n" + str(trapezodial(dx, y)))