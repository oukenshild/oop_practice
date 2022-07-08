import statistics

# Создаём класс студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Задание 2 — выставление оценок лекторов студентами
    def rate_put(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
        else:
            return 'Ошибка'

    # Задание 3.2 — средняя оценка студента
    def _mid_grade(self):
        some_grades = []
        for grade in self.grades.values():
            some_grades.extend(grade)
        result = sum(some_grades) / len(some_grades)
        self.mid_grade = result
        return result

    # Задание 3.1 — перегрузка __str__ у студентов
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._mid_grade()}' \
              f'\nКурсы в процессе изучения: {" ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res

    # Задание 3.2 — сравнение средних оценок студентов
    def __lt__(self, other):
        if not isinstance(other_student, Lecturer):
            print('Можно сравнивать только студентов!')
            return
        elif self.mid_grade() > other_student.mid_grade():
            return f'\n{self.name} {self.surname} имеет среднюю оценку за лекции выше чем {other_student.name} {other_student.surname}'
        else:
            return f'\n{other_student.name} {other_student.surname} имеет среднюю оценку за лекции выше чем {self.name} {self.surname}'


# Создаём родительский класс преподавателей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Создаём дочерний класс лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_grades = {}

    def _mid_grade(self):
        some_grades = []
        for grade in self.courses_grades.values():
            some_grades.extend(grade)
        result = sum(some_grades) / len(some_grades)
        self.mid_grade = result
        return result

    # Задание 3.1 — перегрузка __str__ у лекторов
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._mid_grade()}'
        return res

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Можно сравнивать только лекторов!')
            return
        elif self._mid_grade() > other_lecturer._mid_grade():
            return f'\n{self.name} {self.surname} имеет среднюю оценку за лекции выше чем {other_lecturer.name} {other_lecturer.surname}'
        else:
            return f'\n{other_lecturer.name} {other_lecturer.surname} имеет среднюю оценку за лекции выше чем {self.name} {self.surname}'


# Создаём дочерний класс проверяющих
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Задание 3.1 — перегрузка __str__ у проверяющих
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


some_student = Student('Миша', 'Козицын', 'мужчина')
some_student.finished_courses += ['C++']
some_student.courses_in_progress += ['Python', 'PHP', 'Java']

other_student = Student('Алеся', 'Заика', 'женщина')
other_student.finished_courses += ['PHP']
other_student.courses_in_progress += ['Java', 'C++', 'Python']

some_lecturer = Lecturer('Михаил', 'Зыгарь')
some_lecturer.courses_attached += ['Python', 'C++']

other_lecturer = Lecturer('Александра', 'Зырянова')
other_lecturer.courses_attached += ['Java', 'PHP']

some_student.rate_put(some_lecturer, 'Python', 5)
other_student.rate_put(some_lecturer, 'C++', 5)
some_student.rate_put(other_lecturer, 'Java', 10)
other_student.rate_put(other_lecturer, 'PHP', 10)

some_reviewer = Reviewer('Григорий', 'Явлинский')
other_reviewer = Reviewer('Александр', 'Бортников')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Java']
some_reviewer.courses_attached += ['C++']
some_reviewer.courses_attached += ['PHP']
other_reviewer.courses_attached += ['Python']
other_reviewer.courses_attached += ['Java']
other_reviewer.courses_attached += ['C++']
other_reviewer.courses_attached += ['PHP']

some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'PHP', 8)
other_reviewer.rate_hw(other_student, 'Java', 10)
other_reviewer.rate_hw(other_student, 'C++', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'PHP', 10)
other_reviewer.rate_hw(other_student, 'Java', 9)
other_reviewer.rate_hw(other_student, 'C++', 8)

print(some_student < other_student)
print(some_lecturer > other_lecturer)
print(some_reviewer)
print(other_reviewer)

students = [some_student, other_student]
lecturers = [some_lecturer, other_lecturer]


def average_rating_students(course, *students):
    list_s = []
    for student in students:
        if student.grades.get(course):
            list_s.extend(student.grades[course])
    print(statistics.mean(list_s))


def average_feedback_lecturers(course, *lecturers):
    list_l = []
    for lecturer in lecturers:
        if lecturer.courses_grades.get(course):
            list_l.extend(lecturer.courses_grades[course])
    print(statistics.mean(list_l))

course = 'Java'
print(average_rating_students(course, some_student, other_student))
print(average_feedback_lecturers(course, some_lecturer, other_lecturer))
