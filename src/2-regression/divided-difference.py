import sys

sys.path.append('../../libs/')
from regression import Regressor

if __name__ == "__main__":
    
    points = [float(x) for x in input("Enter points: ").split(' ')]
    values = [float(x) for x in input("Enter values: ").split(' ')]
    polynomial = Regressor(points, values)

    while input("You wish to add a new point (y/n) ") == 'y':
        point = [float(coord) for coord in input("Please enter the coordinates of the new point: ").split(' ')]
        polynomial.appendPoint(point[0], point[1])