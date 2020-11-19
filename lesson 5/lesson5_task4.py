#lesson5_task4 Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


rus_translation = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text_4.txt', 'r', encoding='utf-8') as my_file:
    for content in my_file:
        content = content.strip().split(' - ')
        new_file.append(rus_translation[content[0]] + ' - ' + content[1]+'\n')
    print(new_file)

with open('text_4_new.txt', 'w') as my_file_new:
    my_file_new.writelines(new_file)
