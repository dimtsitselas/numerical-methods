"""
This file implements the divided difference method 
used in interpolating a polymial given some of its points
The user is first asked to give the x coordinates (points)
of these points and then the y coordinates (values)
Afted finding the requested polynomial the user has the option
to add new points.
""" 
import sys

sys.path.append('../../libs/')
from interpolation import Interpolator

if __name__ == "__main__":
    points = [float(x) for x in input("Enter points: ").split(' ')]
    values = [float(x) for x in input("Enter values: ").split(' ')]
    polynomial = Interpolator(points, values)
    print(str(polynomial))

    while input("You wish to add a new point (y/n) ") == 'y':
        point = [float(coord) for coord in input("Please enter the coordinates of the new point: ").split(' ')]
        polynomial.update(point)
        print(str(polynomial))
