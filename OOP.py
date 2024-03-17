class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rating_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        grade = []
        for v in self.grades.values():
            grade.extend(v)
        result = sum(grade) / len(grade)
        return result

    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: "
                f"{round(self._average_grade(), 2)} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        return self._average_grade() < other._average_grade()

student_1 = Student("Ilya", "Titov", "мужской")
student_1.finished_courses += ['Введение в програмирование']
student_1.courses_in_progress += ['Python']


student_2 = Student("Alex", "Banov", "мужской")
student_2.finished_courses += ['Введение в програмирование']
student_2.courses_in_progress += ['Git']


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


mentor_1 = Mentor("Lubov", "Ivanova")
mentor_2 = Mentor("Dima", "Volkov")


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        grade = []
        for v in self.grades.values():
            grade.extend(v)
        result = float(sum(grade) / len(grade))
        return result

    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: "
                f"{round(self._average_grade(), 2)}")

    def __lt__(self, other):
        return self._average_grade() < other._average_grade()


lecturer_1 = Lecturer("Aslan", "Turov")
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2 = Lecturer("Timur", "Baziev")
lecturer_2.courses_attached += ['Git', 'Python']

student_1.rating_lecturer(lecturer_1, 'Python', 9)
student_1.rating_lecturer(lecturer_1, 'Python', 8)
student_1.rating_lecturer(lecturer_1, 'Python', 7)

student_2.rating_lecturer(lecturer_2, 'Git', 9)
student_2.rating_lecturer(lecturer_2, 'Git', 8)
student_2.rating_lecturer(lecturer_2, 'Git', 8)

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} '\n' Фамилия: {self.surname}"



reviewer_1 = Reviewer("Dmitry", "Pupkov")
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)

reviewer_2 = Reviewer("Petya", "Kop")
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 8)

print(f'Перечень студентов:\n{student_1}\n\n{student_2}\n\n')

print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n')

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def average_grade_student_HW(student_list, course_name):
    sum_grade = 0
    count_grade = 0
    for student in student_list:
        if course_name in student.courses_in_progress:
            sum_grade += sum(student.grades.get(course_name, []))
            count_grade = len(student.grades.get(course_name, []))
        average_for_sum = sum_grade / count_grade
        return average_for_sum


def lecturer_rating(lecturer_list, course_name):
    sum_grade = 0
    count_grade = 0
    for lect in lecturer_list:
        if course_name in lect.courses_attached:
            sum_grade += sum(lect.grades.get(course_name, []))
            count_grade += len(lect.grades.get(course_name, []))
    average_for_sum = sum_grade / count_grade
    return average_for_sum


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {round(average_grade_student_HW(student_list, 'Python'), 2)}")
print(f"Средняя оценка для всех лекторов по курсу {'Git'}: {round(lecturer_rating(lecturer_list, 'Git'), 2)}")