# lesson2 task1
my_list = [3.5, 2.8, 'abc', [2, 3, False], True, 'Table!', {4, 234, 45.8, "text", "word", "el", True, None}, 'abrakadabra', {"key_1": 500, 2: 400, "key_3": True, 4: None}, 0]
length = len(my_list)
i=0
print(f'В списке: {length} элементов:')
for i in range(length):
    print(f'{i+1}-й элемент --> {my_list[i]} тип --> {type(my_list[i])}')
