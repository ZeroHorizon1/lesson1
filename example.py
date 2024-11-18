grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]   # список list
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                         # множество set
students = list(students)                                                            # перевод множества в список
sorted_students = sorted(students)                                                   # сортировка списка в алфавитном порядке
# print(sorted_students)
sorted_students = tuple(sorted_students)                                             # перевод списка в кортеж
# print (type(sorted_students))

a1 = sum(grades[0]) / len(grades[0])                                                 # вычисление среднего арифметического в элементах списка
a2 = sum(grades[1]) / len(grades[1])                                                 # вычисление среднего арифметического в элементах списка
a3 = sum(grades[2]) / len(grades[2])                                                 # вычисление среднего арифметического в элементах списка
a4 = sum(grades[3]) / len(grades[3])                                                 # вычисление среднего арифметического в элементах списка
a5 = sum(grades[4]) / len(grades[4])                                                 # вычисление среднего арифметического в элементах списка
new_grades = [a1, a2, a3, a4, a5]                                                    # создание переменной с обновленным списком
grades = new_grades                                                                  # присваивание значений обновленного списка оригинальному списку
# print (grades)

dict = {sorted_students[0] : grades[0],                                             # присваивание ключам из упорядоченного кортежа значений из списка
        sorted_students[1] : grades[1],                                             # присваивание ключам из упорядоченного кортежа значений из списка
        sorted_students[2] : grades[2],                                             # присваивание ключам из упорядоченного кортежа значений из списка
        sorted_students[3] : grades[3],                                             # присваивание ключам из упорядоченного кортежа значений из списка
        sorted_students[4] : grades [4]                                             # присваивание ключам из упорядоченного кортежа значений из списка
}
print (dict)