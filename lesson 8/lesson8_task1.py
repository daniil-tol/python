# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года
class Data:
    def __init__(self, day_month_year):
        #функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
        self.day_month_year = str(day_month_year)

    @classmethod
    # декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число»
    def extract(cls, day_month_year):
        my_date = []
        a = [my_date.append(i) for i in day_month_year.split() if i != '-']
        return int(my_date[0]), int(my_date[1]), int(my_date[2])




    @staticmethod
    # с декоратором @ staticmethod, должен проводить валидацию числа, месяца и года
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Дата прошла валидацию'
                else:
                    return f'Некорректный год'
            else:
                return f'Некорректный месяц'
        else:
            return f'Некорректный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('29 - 11 - 2020')
print(today)
print(Data.extract('29 - 11 - 2020'))
print(Data.valid(19, 11, 2015))
print(Data.valid(32, 11, 2020))
print(today.valid(11, 13, 2020))
print(today.valid(29, 11, 2021))
