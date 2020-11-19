#lesson_task3 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
with open('text_3.txt', 'r', encoding='utf-8') as my_f:
    content = my_f.read()
    print(f'Сожержимое файла file_3.txt:\n{content}')
    my_f.seek(0)
    i = 1
    my_list_stroka = []
    name = []
    for stroka in my_f:
        my_list_stroka = stroka.strip().split()
        if float(my_list_stroka[1]) < 20000.0:
            name.append(my_list_stroka[0])
    print(f'\nВ фале tile_3.txt. {len(name)} - сотрудников имеют оклад менее 20 тыс их фамилии:')
    for surname in name:
        print(f'{i}. {surname}')
        i+=1