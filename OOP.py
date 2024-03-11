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

    def _average_grade(self, grades):
        grade = []
        for a, v in grades.items():
            grade += v
        return sum(grade) / len(grade)

    def __str__(self):
        return (f"Имя: {self.name} '\n' Фамилия: {self.surname} '\n' Средняя оценка за домашние задания: "
                f"{float(Student._average_grade())} '\n' Курсы в процессе изучения: {', '.join(self.courses_in_progress)} '\n' "
                f"Заверщенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        return self._average_grade() < other._average_grade()

student_1 = Student("Ilya", "Titov", "мужской")
student_1.finished_courses += ['Введение в програмирование']
student_1.courses_in_progress += ['Python']
student_1.rating_lecturer(lecturer_1, 'Python', '9')
student_1.rating_lecturer(lecturer_1, 'Python', '8')
student_1.rating_lecturer(lecturer_1, 'Python', '7')

student_2 = Student("Alex", "Banov", "мужской")
student_2.finished_courses += ['Введение в програмирование']
student_2.courses_in_progress += ['Git']
student_2.rating_lecturer(lecturer_2,'Git', '9')
student_2.rating_lecturer(lecturer_2,'Git', '8')
student_2.rating_lecturer(lecturer_2,'Git', '8')
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


mentor_1 = Mentor("Lubov", "Ivanova")
mentor_2 = Mentor("Dima", "Volkov")

class Lecturer(Mentor):
    grades = {}

    def _average_grade(self, grades):
        grade = []
        for a, v in grades.items():
            grade += v
        return sum(grade) / len(grade)

    def __str__(self):
        return (f"Имя: {self.name} '\n' Фамилия: {self.surname} '\n' Средняя оценка за лекции: "
                f"{float(Lecturer._average_grade())}")

    def __lt__(self, other):
        return self._average_grade() < other._average_grade()


lecturer_1 = Lecturer("Aslan", "Turov")
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2 = Lecturer("Timur", "Baziev")
lecturer_2.courses_attached += ['Git', 'Python']

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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

reviewer_1 = Reviewer("Dmitry", "Pupkov")
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)

reviewer_2 = Reviewer("Petya", "Kop")
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_1, 'Git', 8)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}')

print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}')

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
def average_grade_student_HW(students, course_name):
    sum_grade = 0
    count_grade = 0
    for student in student_list:
        if student.courses_in_progress == [course_name]:
            sum_grade += student._average_grade
            count_grade += 1
    average_for_sum = sum_grade / count_grade
    return  average_for_sum

def lecturer_rating(lecturer_list, course_name):
    sum_grade = 0
    count_grade = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_grade += lect._average_grade
            count_grade += 1
    average_for_sum = sum_grade / count_grade
    return average_for_sum

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {average_grade_student_HW(student_list, 'Python')}")
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")