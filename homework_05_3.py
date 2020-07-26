# Задание 3. В этом файле две задачи. Задача 3 и следующая задача, которая на сайте без номера.

# Первая часть. Список фамилий с зарплатами находится в файле file_for_task_3_salaries.txt
employee_list = []
i = 0
summ = 0
try:
    with open("file_for_task_3_salaries.txt", encoding=' utf-8') as file_obj:
        for line in file_obj:
            person = line.split()[0]
            salary = float(line.split()[1])
            if (salary < 20000): print(person)
            i += 1
            summ += salary

except IOError:
    print("Ошибка ввода-вывода.")

print(f"Средняя зарплата равна: {round(summ / i, 2)}")

# Вторая часть. Файл с английскими числительными file_for_task_3_numbers.txt

in_file = open('file_for_task_3_numbers.txt', encoding='utf-8')
out_file = open('file_for_task_3_russian.txt', 'w')
russian_numbers = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}  # Словарь русских числительных

for line in in_file:
    number = int(line.split('—')[1])  # Получаем текущий номер
    string = russian_numbers.setdefault(number) + ' — ' + str(number)  # Формируем строку для файла на русском
    print(string, file=out_file)  # Записываем строку в файл

in_file.close()
out_file.close()
