import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        """Повертає площу прямокутника."""
        return self.width * self.height

    def __eq__(self, other):
        """Порівнює площі двох прямокутників."""
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        """Додає площі двох прямокутників і повертає новий прямокутник із сумарною площею."""
        if isinstance(other, Rectangle):
            new_area = self.get_square() + other.get_square()
            # Підбираємо сторони нового прямокутника: одна сторона — корінь, інша — це площа/сторона
            new_width = math.sqrt(new_area)
            new_height = new_area / new_width
            return Rectangle(new_width, new_height)
        return NotImplemented

    def __mul__(self, n):
        """Множить площу прямокутника на число і повертає новий прямокутник."""
        if isinstance(n, (int, float)):
            new_area = self.get_square() * n
            new_width = math.sqrt(new_area)
            new_height = new_area / new_width
            return Rectangle(new_width, new_height)
        return NotImplemented

    def __str__(self):
        """Повертає рядкове представлення прямокутника."""
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"


# Перевірка
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

# Тести
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2  # Додавання площ
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4  # Множення площі на 4
assert r4.get_square() == 32, 'Test4'

# Порівняння площ двох прямокутників
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

# Виведення результатів
print(r1)  # Rectangle(width=2, height=4, area=8)
print(r2)  # Rectangle(width=3, height=6, area=18)
print(r3)  # Rectangle(width=5.099, height=5.098, area=26)
print(r4)  # Rectangle(width=5.656, height=5.656, area=32)
