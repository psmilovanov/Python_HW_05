# Задание 4. Записывает в файл file_for_task_4.txt числа через пробел. Потом читает эти числа и вычисляет сумму.

from random import randint

count_of_numbers = randint(1, 20)

with open('file_for_task_4.txt', 'w') as file_obj:
    for i in range(count_of_numbers):
        string = str(randint(1, 100)) + ' '
        file_obj.write(string)
summ = 0
with open('file_for_task_4.txt', 'r') as file_obj:
    string = file_obj.read()
    numbers = string.split()
    for i in range(len(numbers)): summ += int(numbers[i])

print(f"Сумма чисел равна {summ}")
