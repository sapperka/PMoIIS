import datetime

class Student:
    def __init__(self, first_name, last_name, birth_date, subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.subjects = subjects

class Subject:
    def __init__(self, name, exam_date, teacher):
        self.name = name
        self.exam_date = exam_date
        self.teacher = teacher

def print_exam_schedule(students):
    print(f"{'Student':<20} {'Subject':<20} {'Exam Date':<20} {'Teacher':<20}")
    print("-" * 80)
    for student in students:
        for subject in student.subjects:
            print(f"{student.first_name} {student.last_name:<20} {subject.name:<20} {subject.exam_date:<20} {subject.teacher:<20}")

if __name__ == "__main__":
    students = [
        Student("Ivanov", "Kirill", datetime.date(2000, 5, 15), [
            Subject("Math", datetime.date(2024, 6, 1), "Lavrenov"),
            Subject("History", datetime.date(2024, 6, 15), "Radeonova"),
        ]),
        Student("Petrova", "Elizaveta", datetime.date(2001, 7, 25), [
            Subject("Math", datetime.date(2024, 6, 1), "Lavrenov"),
            Subject("Chemistry", datetime.date(2024, 6, 10), "Hohlov"),
        ]),
    ]

    print_exam_schedule(students)
