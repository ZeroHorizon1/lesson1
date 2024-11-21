first = int(input())                                        # Вводим первое значение
second = int(input())                                       # Вводим второе значение
third = int(input())                                        # Вводим третье значение
if first == second == third:                                # Выполняем первый цикл проверки на равность всех значений
    print ('3')                                             # Выводим в консоль результат
elif first == second or second == third or third == first:  # Выполняем второй цикл проверки на равность хотя бы двух значений
    print ('2')                                             # Выводим в консоль результат
elif first != second or second != third or third != first:  # Выполняем третий цикл проверки на наличие равных значений
    print ('0')                                             # Выводим в консоль результат