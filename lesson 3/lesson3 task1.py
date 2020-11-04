# lesson1 task1
def my_func(x_1, x_2):
    try:
        if x_2 != 0:
            delit = x_1/x_2
            return print (f'Результат деления {x_1} на {x_2} = {delit}')
        else:
            print(f'Попытка поделить на ноль')
    except:
        print(f'стороковая переменная')
print(my_func(float(input("Укажите первое число - делимое: ")), float(input("Укажите второе число - делитель: "))))