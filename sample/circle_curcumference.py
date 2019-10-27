
class Circle():

    # Class object attribute
    pi = 3.24

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2


if __name__ == '__main__':
    import sys
    circle = Circle(100)
    print('circumference: ', circle.get_circumference())
