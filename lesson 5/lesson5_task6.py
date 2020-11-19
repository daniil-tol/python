#lesson5 task6
with open('text_6.txt','r',encoding='utf-8') as my_file:
    content = my_file.read()
    print(f'Сожержимое файла text_6.txt:\n{content}\n')
    my_file.seek(0)
    for i in my_file:
        name = i[:i.index(':')]
        numbers = i[i.index(':'):]
        numbers = ''.join([(j if j in '1234567890'else ' ') for j in numbers]).split()
        numbers_sum = sum(map(int, numbers))
        print(f'Предмет {name.upper()} и количество занятий по нему {numbers_sum}')