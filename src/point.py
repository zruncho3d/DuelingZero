# # https://stackoverflow.com/questions/7685984/add-method-that-works-with-either-a-point-object-or-a-tuple
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("unsupported operand type(s) for +: 'Point' and '{0}'".format(type(other)))

    def copy(self):
        return Point(self.x, self.y)

    def __repr__(self):
        return 'Point ({0}, {1})'.format(self.x, self.y)
