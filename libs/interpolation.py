class Regressor():

    def __init__(self, points, values):
        self.n = len(points)
        self.x = points
        self.y = values

        self.table = [[0 for x in range(self.n)] for y in range(self.n)]
        self._initTable()
    
    def _initTable(self):


    def update(self, point):
        self.x.extend(point[0])
        self.y.extend(point[1])
        self.n += 1

        # Extend existing rows
        for row in self.table:
            row.extend([0])
        
        # Add new row for the new point
        self.table.extend([0 for y in range(self.n)])

        # Necessary initialization
        self.table[-1][0] = self.y[-1]

        # Fill table
        for c in range(1, self.n):
            self.table[-1][c] = (self.table[-1][c-1] - self.table[-2][c-1])/float((self.x[-1] - self.x[-c-1]))
