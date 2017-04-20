import sys

sys.path.append('../../libs/')
from polynomials import LagrangePolynomial

def lagrange_iterpolation(points, values):
    LP = LagrangePolynomial(values, points)
    print(str(LP))

if __name__ == "__main__":
    points = [float(x) for x in input("Enter points: ").split(' ')]
    values = [float(x) for x in input("Enter values: ").split(' ')]

    lagrange_iterpolation(points, values)