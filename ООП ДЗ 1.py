class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):   # Добавления курса
        self.finished_courses.append(course_name)   

    def rate_lecturer(self, teacher, course, grade):   # ставить оценки лекторам
        if isinstance(teacher, Lecturer) and course in teacher.courses_attached and course in self.courses_in_progress:
            if course in teacher.lec_grades:
                teacher.lec_grades[course] += [grade]
            else:
                teacher.lec_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_stud(self):   # Средняя оценка из всех оценок по каждому студенту
        self.all_grades = []
        for answer in self.grades.values():
            self.all_grades.extend(answer)
        return round(sum(self.all_grades) / len(self.all_grades), 2)

    def __lt__(self, other):   # сравнение средних оценок студентов
        if not isinstance(other, Student):
            print("Не студент.")
            return
        return self.average_grade_stud() < other.average_grade_stud()

    def __str__(self):   #вывод
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average_grade_stud()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):   # Лекторы
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
        self.lec_grades = {}

    def average_grade_ment(self):   # Средняя оценка из всех оценок по каждому лектору
        self.all_grades = []
        for answer in self.lec_grades.values():
            self.all_grades.extend(answer)
        return round(sum(self.all_grades) / len(self.all_grades), 2)

    def __lt__(self, other):   # сравнение средних оценок лекторов
        if not isinstance(other, Lecturer):
            print("Не находится в преподавателях")
            return
        return self.average_grade_ment() < other.average_grade_ment()

    def __str__(self):   #вывод
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade_ment()}'
        return res


class Reviewer(Mentor):   # Эксперты, проверяющие домашние задания
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached

    def __str__(self):   #вывод
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):   #ставить оценки студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


some_student_1 = Student('Илья', 'Дьяконов', 'м')
some_student_2 = Student('Арья', 'Старк', 'ж')
some_student_1.courses_in_progress += ['Python', 'Java']
some_student_2.courses_in_progress += ['Python', 'Java']
some_student_1.finished_courses += ['Вводный модуль']
some_student_2.finished_courses += ['Английский для IT']

some_lector_1 = Lecturer('Олег', 'Булыгин', 'Python')
some_lector_2 = Lecturer('Адилет', 'Асанкожоев', 'Java')
some_reviewer_1 = Reviewer('Питер', 'Паркер', ['Python', 'Java'])
some_reviewer_2 = Reviewer('Джони', 'Сильверхенд', ['Python', 'Java'])

students_list = [some_student_1, some_student_2]
lectors_list = [some_lector_1, some_lector_2]

some_student_1.rate_lecturer(some_lector_1, 'Python', 9)
some_student_1.rate_lecturer(some_lector_2, 'Java', 8)
some_student_2.rate_lecturer(some_lector_1, 'Python', 8)
some_student_2.rate_lecturer(some_lector_2, 'Java', 10)

some_reviewer_1.rate_hw(some_student_1, 'Python', 7)
some_reviewer_1.rate_hw(some_student_1, 'Java', 7)
some_reviewer_1.rate_hw(some_student_2, 'Python', 9)
some_reviewer_1.rate_hw(some_student_2, 'Java', 10)

some_reviewer_2.rate_hw(some_student_1, 'Python', 6)
some_reviewer_2.rate_hw(some_student_1, 'Java', 9)
some_reviewer_2.rate_hw(some_student_2, 'Python', 8)
some_reviewer_2.rate_hw(some_student_2, 'Java', 7)

print(some_student_1)
print()
print(some_student_2)
print()
print(some_lector_1)
print()
print(some_lector_2)
print()
print(some_reviewer_1)
print()
print(some_reviewer_2)
print()
print(f'Сравнение оценок между студентами:')
print(some_student_1 < some_student_2)
print()
print(f'Сравнение оценок между лекторами:')
print(some_lector_1 < some_lector_2)
print()
print(some_student_1.average_grade_stud())
print(some_student_2.average_grade_stud())
print(some_lector_1.average_grade_ment())
print(some_lector_2.average_grade_ment())

students_list = [some_student_1, some_student_2]

def get_st(student, course):
    some_list = []
    for person in student:
        for key, value in person.grades.items():
            if key == course:
                some_list += value
    return f'Средняя оценка у студентов по предмету {course}: {round(sum(some_list) / len(some_list), 2)}'

print(get_st(students_list, 'Python'))
print(get_st(students_list, 'Java'))

lecturer_list = [some_lector_1, some_lector_2]

def get_lec(lecturer, course):
    some_list = []
    for person in lecturer:
        for key, value in person.lec_grades.items():
            if key == course:
                some_list += value
    return f'Средняя оценка у студентов по предмету {course}: {round(sum(some_list) / len(some_list), 2)}'

print(get_lec(lecturer_list, 'Python'))
print(get_lec(lecturer_list, 'Java'))