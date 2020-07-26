# Задание 5. Данные в файле file_for_task_5.txt

kind_of_lesson = [['(л)', len('(л)')], ['(пр)', len('(пр)')],
                  ['(лаб)', len('(лаб)')]]  # список сокращений для видов занятий и число букв в сокращении
numeric = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')  # цифры
dict_of_lesson = {}  # требуемый словарь

with open("file_for_task_5.txt", "r", encoding="utf-8") as file_obj:
    for string in file_obj:
        summ = 0
        name = string.split(':')[0]  # Находим имя предмета

        string_cut = string.split(':')[1]
        # остаток строки после удаления имени предмета, будет изменяться после нахождения количестов часов
        for ind, el in enumerate(kind_of_lesson):
            # обход по нумерованному списку предметов
            find_less = string_cut.find(el[0])  # поиск названия из нумерованного списка

            if (find_less != -1):
                # в переменной string_less должно остаться количесвто часов данного вида занятий
                string_less = string_cut[:find_less]

                for i in range(len(string_less)):
                    if (string_less[i] not in numeric): new_string_less = string_less[i:]
                string_less = new_string_less

                try:
                    summ += int(string_less)
                except:
                    print("В исходном файле что-то не так")
                string_cut = string_cut[find_less + el[1]:]
                # уменьшение строки string_cut

        dict_of_lesson.update({name: summ})  # обновление словаря

print(dict_of_lesson)
