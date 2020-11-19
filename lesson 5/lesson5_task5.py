#lesson5_task5 Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('text_5.txt', 'w', encoding='utf-8') as my_f:
    my_list = []
    while True:
        line = input(f'Введите набор чисел, разделенных пробелом или зкончание ввод Enter. \n')
        if line == '':
            my_f.writelines(my_list)
            print(f'Вы закончили ввод данных в документ text_5.txt')
            a = sum([int(item) for item in my_list])
            print(f'Cумма чисел в файле  {a}')
            exit()
        else:
            my_list = my_list + line.split()
            print(my_list)

# разобранный вариант решения

from random import randint

with open('file_5.txt','w+',encoding='utf-8') as the_file:
    the_file.write(' '.join([str(randint(1, 10)) for _ in range(100)]))
    the_file.seek(0)
    print(sum(map(int, the_file.readline().split())))