class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        for elem in self.grades.values():
            res_1 = sum(elem) / len(elem)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {round(res_1, 2)}\nКурсы в процессе: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент.')
            return
        for i in self.grades.values():
            self.res_1 = sum(i) / len(i)
        for j in other.grades.values():
            other.res_2 = sum(j) / len(j)
        return self.res_1 < other.res_2



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Reviewer(Mentor):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


    def __str__(self):
        for elem in self.grades.values():
            res_1 = sum(elem) / len(elem)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {round(res_1, 2)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не Лектор.')
            return
        for i in self.grades.values():
            self.res_1 = sum(i) / len(i)
        for j in other.grades.values():
            other.res_2 = sum(j) / len(j)
        return self.res_1 < other.res_2


# Экземпляр студента_1
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']


# Экземпляр студента_2
bad_student = Student('Alex', 'Frivolous', 'your_gender')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Engineering']
bad_student.finished_courses += ['Введение в программирование']


# Проверяющий
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# Оценки для студента_1
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# Оценки для студента_2
cool_reviewer.rate_hw(bad_student, 'Python', 5)
cool_reviewer.rate_hw(bad_student, 'Python', 7)
cool_reviewer.rate_hw(bad_student, 'Python', 6)



# Лектор_1
great_lecturer = Lecturer('Anthony', 'Robbins')
great_lecturer.courses_attached += ['Python']

# Лектор_2
good_lecturer = Lecturer('Tony', 'Stark')
good_lecturer.courses_attached += ['Engineering']


# Оценка для лектора_1
best_student.rate_lecturers(great_lecturer, 'Python', 10)
best_student.rate_lecturers(great_lecturer, 'Python', 8)
best_student.rate_lecturers(great_lecturer, 'Python', 9)

# Оценка для лектора_2
bad_student.rate_lecturers(good_lecturer, 'Engineering', 10)
bad_student.rate_lecturers(good_lecturer, 'Engineering', 9)
bad_student.rate_lecturers(good_lecturer, 'Engineering', 9)


print(best_student.grades)
print(bad_student.grades)

print(great_lecturer.grades)
print(good_lecturer.grades)

print(cool_reviewer)
print(great_lecturer)
print(good_lecturer)
print(best_student)
print(bad_student)

print(best_student > bad_student)
print(good_lecturer > great_lecturer)


# Функции подсчета средней оценки
students = [best_student, bad_student]
lecturers = [great_lecturer, good_lecturer]


def students_grade(students, course):
    count = 0
    sum_gr = 0
    for student in students:
        if course in student.grades:
            count += len(student.grades[course])
            sum_gr += sum(student.grades[course])
    return round((sum_gr / count), 2)

print(students_grade(students, 'Python'))

def lecturers_grade(lecturers, course):
    count = 0
    sum_gr = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            count += len(lecturer.grades[course])
            sum_gr += sum(lecturer.grades[course])
    return round((sum_gr / count), 2)

print(lecturers_grade(lecturers, 'Python'))

