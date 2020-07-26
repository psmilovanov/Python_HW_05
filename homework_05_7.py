# Задание 7

dict_company = {}
dict_average_prof = {}

num_profit_comp = 0
summ_profit = 0

with open("file_for_task_7.txt", "r", encoding="utf-8") as file_obj:
    for list in file_obj:
        data_list = list.split()
        print(data_list)
        name = data_list[0]

        try:
            profit = float(data_list[2]) - float(data_list[3])
        except:
            print(f"В исходном файле ошибка в строке {list}")

        if (profit >= 0):
            num_profit_comp += 1
            summ_profit += profit

        dict_company.update({name: profit})

final_list = [dict_company, {'average_profit': round(summ_profit / num_profit_comp, 2)}]

print(f"В файл jsonfile_for_task_7.json записан требуемый список: \n {final_list}. ")

import json

with open("jsonfile_for_task_7.json", "w") as file_obj:
    json.dump(final_list, file_obj)
