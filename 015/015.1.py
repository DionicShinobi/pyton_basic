import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return math.isclose(self.get_square(), other.get_square())
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            total_area = self.get_square() + other.get_square()
            side_length = math.sqrt(total_area)
            return Rectangle(side_length, side_length)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            new_area = self.get_square() * n
            side_length = math.sqrt(new_area)
            return Rectangle(side_length, side_length)
        return NotImplemented

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# Тестування
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert math.isclose(r3.get_square(), 26), 'Test3'

r4 = r1 * 4
assert math.isclose(r4.get_square(), 32), 'Test4'

assert Rectangle(2, 4) == Rectangle(2, 4), 'Test5'
assert Rectangle(2, 4) != Rectangle(3, 6), 'Test6'
