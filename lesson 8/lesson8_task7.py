# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав
# экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class Complex:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма: {self.a}+({self.b})i + {other.a}+({other.b})i:')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Умножение: {self.a}+({self.b})i * {other.a}+({other.b})i:')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.a * other.b +self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a}+({self.b})i'


z_1 = Complex(5, 4)
z_2 = Complex(6, 9)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)