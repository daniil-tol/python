#lesson5 task7

import json

with open('text_7.txt','r',encoding='utf-8') as my_file:
    content = my_file.read()
    print(f'Сожержимое файла text_7.txt:\n{content}\n')
    my_file.seek(0)
    profit_dict = dict()
    new1_profit_dict = dict()
    new2_profit_dict = dict()
    average_profit = dict()
    damages_profit = dict()
    s = 0
    b = 0
    i = 0
    j = 0
    for stroka in my_file:
        stroka_file = stroka.split()
        profit_dict[stroka_file[0]] = (int(stroka_file[2])-int(stroka_file[3]))
    # print(profit_dict)

    for key, value in profit_dict.items():
        if value > 0:
            new1_profit_dict[key] = value
            s = s + value
            i = i + 1
        else:
            new2_profit_dict[key] = value
            b = b + value
            j = j + 1

    average_profit['average_profit'] = round(s / i, 2)
    damages_profit['damages_profit'] = round((-b )/ j, 2)

    result_1 = [new1_profit_dict, average_profit]
    result_2 = [new2_profit_dict, damages_profit]

    print(f'Фимы раюотающие с прибылью {result_1}')
    print(f'Фимы раюотающие в убыток {result_2}')

    with open('text_7_new.txt','w', encoding='utf-8') as write_file:
        print(f'Результат (Фимы раюотающие с прибылью) записан в файл text_7_new.txt:')
        json.dump(result_1, write_file, ensure_ascii=False,indent=4)

