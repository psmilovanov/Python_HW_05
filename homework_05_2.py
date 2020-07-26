# Задание 2. Определяет количесвто строк и чисел в каждой строке в файле file_for_task_2.txt

str_number = [0]
i = 0
try:
    with open("file_for_task_2.txt") as file_obj:
        for line in file_obj:
            str_number[0] += 1
            i += 1
            print(f"В строке {i} слов : {len(line.split())}")
except IOError:
    print("Ошибка ввода-вывода.")

print(f"Число строк в файле file_for_task_2: {str_number[0]}")
