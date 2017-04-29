"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ interpolation.py ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module has classes for some elementary polynomial representations such as 
exponential form, center form, newton form, and lagrange form.
"""

from polynomials import NewtonPolynomial

class Interpolator():
    """This is a basic class of an internpolator

    We initialize the interpolator with some points and it provides us with a
    polynomial that passes through all of those points.abs

    This interpolator is implemented with the method of *divided differences*,
    hence you can dynamically add points and let the class recalculate the
    interpolation polynomial. 
    """

    def __init__(self, points, values):
        """Store the points and find divided differences."""

        if len(points) != len(values):
            raise AttributeError("points and values don't have the same length")

        self.n = len(points)    # number of points
        self.x = points         # x coordinates
        self.y = values         # y coordinates

        # Containes the divided differences
        self.table = [[0 for x in range(self.n)] for y in range(self.n)]
        self._initTable()

        # It's our interpolation polynomial
        self.NP = self._buildPoly()

    def __str__(self):
        """Returns the interpolation polynomial in string form"""

        return str(self.NP)

    def update(self, point):
        self.x.append(point[0])
        self.y.append(point[1])
        self.n += 1

        # Extend existing rows
        for row in self.table:
            row.extend([0])
        
        # Add new row for the new point
        self.table.extend([[0 for y in range(self.n)]])

        # Necessary initialization
        self.table[-1][0] = self.y[-1]

        # Fill table
        for c in range(1, self.n):
            self.table[-1][c] = (self.table[-1][c-1] - self.table[-2][c-1])/float((self.x[-1] - self.x[-c-1]))

        # Update Polynomial
        self.NP = self._buildPoly()
    
    def _initTable(self):
        """Complete the table of divided differences"""

        # Initialize table
        for r in range(self.n):
            self.table[r][0] = self.y[r]

        # Fill table
        for c in range(1, self.n):
            for r in range(c, self.n):
                self.table[r][c] = (self.table[r][c-1] - self.table[r-1][c-1])/float((self.x[r] - self.x[r-c]))

    def _buildPoly(self):
        """Calculates and returns the interpolation"""

        # Coefficients are accually the elements of the main diagonal of table
        coeffs = [self.table[i][i] for i in range(self.n)]

        # We build our Newton Polynomial
        NP = NewtonPolynomial(coeffs, self.x)

        return NP
