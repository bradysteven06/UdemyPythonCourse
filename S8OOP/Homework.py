class Line:

    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        # tuple unpacking
        x1, y1 = self.coord1
        x2, y2 = self.coord2

        # equation for distance between two points
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coord1
        x2, y2 = self.coord2

        return (y2 - y1) / (x2 - x1)


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius)**2

    def surface_area(self):
        top = 3.14 * (self.radius**2)
        return (2*top) + (2*3.14*self.radius*self.height)


if __name__ == '__main__':

    # EXAMPLE OUTPUT

    coordinate1 = (3, 2)
    coordinate2 = (8, 10)

    li = Line(coordinate1, coordinate2)

    print(li.distance())
    print(li.slope())

    # EXAMPLE OUTPUT
    c = Cylinder(2, 3)

    print(c.volume())
    print(c.surface_area())

