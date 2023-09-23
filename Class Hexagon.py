#  The class Hexagon represents the regular hexagons (all sides are equal in length and all angles equal 120 degrees).
#  The only parameter needed to create a regular hexagon is the length of its side.
#  Create a method get_area that calculates the area of the hexagon


import math


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    # create get_area here
    def get_area(self):
        return round((3 * math.sqrt(3) * self.side_length**2) / 2, 3)


hexagon1 = Hexagon(5.4)
print(f'Area of hexagon1 is {hexagon1.get_area()} with side length of {hexagon1.side_length}')
