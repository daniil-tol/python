# lesson4_task4
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
my_tuple = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_obj = [el for el in my_tuple if my_tuple.count(el) == 1]
print(f'Результат: {new_obj}')

my_tuple_1 = input(f'Введите список чисел разделенных пробелом: ').split()
new_obj_1 = [el for el in my_tuple_1 if my_tuple_1.count(el) == 1]
print(f'Результат: {new_obj_1}')