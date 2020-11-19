#lesson5_task1 Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
with open('file_1.txt', 'w', encoding='utf-8') as my_f:
    my_list = []
    while True:
        line = input(f'Введите текст: \n')
        if line == '':
            my_f.writelines(my_list)
            print(f'Вы закончили ввод данных в документ file_1.txt')
            exit()
        else:
            my_list.append(line + '\n')
            print(my_list)