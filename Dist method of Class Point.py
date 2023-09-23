#  Calling two instances of the same Class
#  perform method dist() on both instances of same Class


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, s_p2):
        return ((self.x - s_p2.x)**2 + (self.y - s_p2.y)**2)**0.5


p1 = Point(1.5, 1)
p2 = Point(1.5, 2)
print(p1.dist(p2))
