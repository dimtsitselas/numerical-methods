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
