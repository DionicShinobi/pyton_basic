# Створюємо користувацький виняток
class GroupLimitError(Exception):
    def __init__(self, message="Неможливо додати студента. Ліміт групи — 10 студентів."):
        super().__init__(message)


# Клас Студент
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"


# Клас Група
class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupLimitError()  # Викидаємо виняток, якщо більше 10 студентів
        self.students.append(student)

    def __str__(self):
        return "\n".join(str(student) for student in self.students)


# Приклад використання
if __name__ == "__main__":
    group = Group()

    # Створюємо 11 студентів
    students = [Student(f"Student{i}", f"Surname{i}") for i in range(11)]

    try:
        # Пробуємо додати всіх студентів до групи
        for student in students:
            group.add_student(student)
            print(f"Студента {student} додано.")

    except GroupLimitError as e:
        print(f"Помилка: {e}")

    print("\nГрупа студентів:")
    print(group)
