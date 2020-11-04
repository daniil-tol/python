# lesson1 task4
def my_func(x, y):
    res = 1
    if x > 0 and y < 0:
        for i in range(abs(y)):
            res *= x
        return print(f'Результат возведения {x} в степень {y} = {round((1 / res), 3)}')
    else:
        print(f'Скоректируйте введенные значения. Второе число должно быть меньше нуля')

print(my_func(int(input(f'Введите действительное положительное число: ')), int(input(f'Введите целое отрицательное число:  '))))
