grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
i = 0
for j in grades:  # Переборка списков с оценками разных учеников
    sum = 0  # Сумма всех оценок у каждого отдельного ученика
    for l in j:  # Переборка оценок из списка с оценками ученика
        sum += l  # Сложение всех оценок ученика
    sum = sum / len(j)  # Ср. балл ученика из суммы всех оценок деленное на их кол-во
    grades[i] = sum  # Замена списка с оценками ученика на средний балл
    i += 1

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_1 = list(students)  # Перевод в множества в список для сортировки
students_1.sort()  # Сортировка списка по алфавиту
grades_students = {}  # Конечный словарь
i = 0
for k in students_1:  # Перебор имен из списка
    grades_students[k] = grades[i]  # Добавляем в словарь пару [имя]: [значение]
    i += 1
print(grades_students)  # Вывод словаря

"""#другой вид кода
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
sum_grades = sum(grades[0]) / len(grades[0])
grades[0] = sum_grades
sum_grades = sum(grades[1]) / len(grades[1])
grades[1] = sum_grades
sum_grades = sum(grades[2]) / len(grades[2])
grades[2] = sum_grades
sum_grades = sum(grades[3]) / len(grades[3])
grades[3] = sum_grades
sum_grades = sum(grades[4]) / len(grades[4])
grades[4] = sum_grades

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_1 = list(students)  # Перевод в множества в список для сортировки
students_1.sort()  # Сортировка списка по алфавиту
grades_students = {}  # Конечный словарь
grades_students[students_1[0]] = grades[0]
grades_students[students_1[1]] = grades[1]
grades_students[students_1[2]] = grades[2]
grades_students[students_1[3]] = grades[3]
grades_students[students_1[4]] = grades[4]
print(grades_students)  # Вывод словаря

"""
