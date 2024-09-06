class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        """Встановлює поточне значення лічильника."""
        if self.min_value <= start <= self.max_value:
            self.current = start
        else:
            raise ValueError(f"Значення {start} поза межами [{self.min_value}, {self.max_value}]")

    def set_max(self, max_max):
        """Встановлює максимальне значення лічильника."""
        if max_max < self.min_value:
            raise ValueError("Максимальне значення не може бути меншим за мінімальне.")
        self.max_value = max_max

    def set_min(self, min_min):
        """Встановлює мінімальне значення лічильника."""
        if min_min > self.max_value:
            raise ValueError("Мінімальне значення не може бути більшим за максимальне.")
        self.min_value = min_min

    def step_up(self):
        """Збільшує поточне значення на 1 до досягнення максимального значення."""
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Достигнуто максимум.")

    def step_down(self):
        """Зменшує поточне значення на 1 до досягнення мінімального значення."""
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Достигнуто мінімум.")

    def get_current(self):
        """Повертає поточне значення лічильника."""
        return self.current


# Тестування
counter = Counter()

# Встановлюємо початкове значення 7
counter.set_current(7)

# Збільшуємо значення на 1 три рази
counter.step_up()
counter.step_up()
counter.step_up()

# Перевіряємо поточне значення
assert counter.get_current() == 10, 'Test1'

# Спроба збільшити значення понад максимум (очікується ValueError)
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнуто максимум

# Перевіряємо поточне значення після винятку
assert counter.get_current() == 10, 'Test2'

# Встановлюємо мінімальне значення на 7
counter.set_min(7)

# Зменшуємо значення на 1 три рази
counter.step_down()
counter.step_down()
counter.step_down()

# Перевіряємо поточне значення
assert counter.get_current() == 7, 'Test3'

# Спроба зменшити значення понад мінімум (очікується ValueError)
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнуто мінімум

# Перевіряємо поточне значення після винятку
assert counter.get_current() == 7, 'Test4'
