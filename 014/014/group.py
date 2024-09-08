from student import Student

class Group:
    def __init__(self, name):
        self.name = name
        self.students = set()

    def add_student(self, student):
        if len(self.students) >= 20:
            raise ValueError("Cannot add more than 20 students to the group")
        self.students.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        return f"Group {self.name}:\n" + "\n".join([str(student) for student in self.students])
