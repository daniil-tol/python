# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return f'{round((divider / denominator), 5)}'
        except:
            return (f"Деление на ноль недопустимо, скоректируйте вводимые данные")

print(DivisionByNull.divide_by_null(1, 0))
print(DivisionByNull.divide_by_null(10, -18))

while True:
    try:
        a = float(input('\nВведите делитель: '))
        b = float(input('Ведите знаменатель: '))
        print(DivisionByNull.divide_by_null(a, b))
    except ValueError:
        print('Буквы не делятся, попробуй вводить числа')



