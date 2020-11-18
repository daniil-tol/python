#lesson5_task2 Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open('file_1.txt', 'r', encoding='utf-8') as my_f:
    content = my_f.read()
    print(f'Сожержимое файла file_1.txt:\n{content}')
    my_f.seek(0)
    i = 1
    simvol = 0
    slova = 0
    for stroka in my_f:
        print(f'В {i}-строке: "{stroka.strip()}"\nСодержиться: {len(stroka.strip())} элемент(а/ов) и {((" ".join([el for el in stroka.strip().split()])).count(" "))+1} слов(о/а) \n')
        i = i + 1
        simvol = simvol + len(stroka.strip())
        slova = slova + (((" ".join([el for el in stroka.strip().split()])).count(" "))+1)
    print(f'В фале tile_1.txt \n{i-1} - строк, {simvol} - символов, {slova} - слов')