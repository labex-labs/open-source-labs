class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return round(3.1416 * (self.radius**2), 4)


radius = int(input())
circle = Circle(radius)
print(circle.area())
