# lesson2 task6
n = int(input('Введите сколько товара у вас в наличии: '))
i = 1
my_product = []
my_list1 = []
my_analys = {}
while i <= n:
     print(f'Введите данные {i} товара')
     my_product = dict({'название': input('Введите название -> '), 'цена': input('Введите цену -> '), 'количество ': input('Введите количество -> '), 'eд': input('Введите единицу измерения -> ')})
     my_list1.append((i, my_product))
     i += 1
print(my_list1)