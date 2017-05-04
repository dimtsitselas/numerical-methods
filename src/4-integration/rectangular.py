import sys

sys.path.append('../../libs/')
from functiontools import function
from integralutil import get_interval_points


if __name__ == "__main__":
    n = int(input("Enter n: "))
    intLimits = [float(x) for x in input("Please enter integration limits: ").split(' ')]
    expr = input("Please give the function to be integrated: ")

    f = function(expr)

    x, y = get_interval_points(n, f, intLimits)
    print(x)
    print(y)