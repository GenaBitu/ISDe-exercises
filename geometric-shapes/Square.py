from Polygon import Polygon;

class Square(Polygon):
    def __init__(self, side):
        self.side = side;
    def perimeter(self):
        return 4 * self.side;
