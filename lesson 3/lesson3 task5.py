# lesson1 task5
result = 0
namber = input(f'Введите строку чисел, разделенных пробелом: ').split()
b = 0
for i in namber:
    try:
        b=b+1
        if i == '!':
            print(f'Summa = {result}. Конец программы')
        else:
            result = result + int(i)
            print(f'+{i}. Summa = {result}')
            if i == namber[-1] and b == len(namber):
                print(namber)
                namber.append(input(f'Summa = {result}. Вы можете дополнить одно число или выбрать завершение работы введя ! '))
                # не разобрался, как можно добавить не одно число, а несколько. Когда вводим несколько чисел он их распознает, как стороковый элемент и выходит из цикла.
                # если вводить одно число все работает
    except ValueError:
        print(f'Введите число или !')