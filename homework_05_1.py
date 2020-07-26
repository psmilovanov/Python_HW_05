# Задание 1.


out_file = open("file_for_task_1.txt", "w")

print("Введите построчно данные для записи в файл file_for_task_1.txt")

str_line = []
while True:
    str = input("Введите новую строку для записи в файл. Пустая строка - конец записи: ")
    if str == '':
        break
    else:
        # str = str + 'n'
        out_file.write(str + '\n')
        # str_line.extend(str)

# out_file.writelines(str_line)
out_file.close()
