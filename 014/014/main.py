from student import Student
from group import Group

if __name__ == "__main__":
    # Створення студентів
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    # Створення групи
    gr = Group('PD1')

    # Додавання студентів до групи
    gr.add_student(st1)
    gr.add_student(st2)

    # Виведення інформації про групу
    print(gr)

    # Перевірка знаходження студента за прізвищем
    assert gr.find_student('Jobs') == st1  # Студент 'Steve Jobs'
    assert gr.find_student('Jobs2') is None  # Неіснуючий студент

    # Видалення студента
    gr.delete_student('Taylor')

    # Виведення інформації після видалення студента
    print(gr)  # Залишився тільки один студент
