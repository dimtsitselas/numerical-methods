class Regressor():

    def __init__(self, points, values):
        self.n = len(points)
        self.x = points
        self.y = values

        self.table = [[0 for x in range(self.n)] for y in range(self.n)]
        self._initTable()
    
    def _initTable(self):