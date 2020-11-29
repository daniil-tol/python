# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Sklad:

    def __init__(self, name, quantity, price, make, year, *args):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.make = make
        self.year = year
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Предмет склада:': self.name, 'Цена за ед:': self.price, 'Количество на складе:': self.quantity, 'Произведено в:': self.make, 'Год:': self.year}

    def __str__(self):
        return f'{self.name}, количество ед {self.quantity}, цена {self.price}, сделано в {self.make}, год {self.year}'

    def reception(self):
        try:
            name_a = input(f'Введите наименование предмета: ')
            quantity_a = int(input(f'Введите количество: '))
            price_a = float(input(f'Введите цену за ед:  '))
            make_a = input(f'Введите где был произведен предмет: ')
            year_a = int(input(f'Введите год, когда был произведен предмет: '))
            unique = {'Предмет склада:': name_a, 'Цена за ед:': quantity_a, 'Количество на складе:': price_a ,'Произведено в:': make_a, 'Год:': year_a}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список: \n {self.my_store}')

        except ValueError:
            return f'Ошибка ввода данных. Данные о количестве, цене за ед и годе выпуска должны бытьчислами.'

        print(f'Для выхода - !, продолжение - Enter')
        a = input()
        if a == '!':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Sklad.reception(self)


class Printer(Sklad):
    def __init__(self, name, quantity, price, make, year, type, speed, duplex_printing):
        super().__init__(name, quantity, price, make, year)
        self.type = type
        self.speed = speed
        self.duplex_printing = duplex_printing

    def to_print(self):
        return f'printer {self.name}, print type {self.type}, speed page/sec {self.speed}, duplex printing {self.duplex_printing}'


class Scanner(Sklad):
    def __init__(self, name, quantity, price, make, year, scan_size):
        super().__init__(name, quantity, price, make, year,)
        self.scan_size = scan_size


    def to_scan(self):
        return f'scanner {self.name}, scan_size {self.scan_size}'


class Copier(Sklad):
    def __init__(self, name, quantity, price, make, year, scan_size, color):
        super().__init__(name, quantity, price, make, year)
        self.scan_size = scan_size
        self.color = color

    def to_copier(self):
        return f'copier {self.name}'

# Printer name, quantity, price, make, year, type, speed, duplex_printing
# Scanner name, quantity, price, make, year, scan_size
# Copier name, quantity, price, make, year, scan_size, color
unit_1 = Printer('HP', 20, 15000, "КИТАЙ", 2013, 'laser', 10, True)
unit_2 = Scanner('Canon', 4, 7500, "КИТАЙ", 2019, 'A4')
unit_3 = Copier('Samsung', 30, 12000, "КОРЕЯ", 2017, 'A4', True)
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())

sklad = Sklad('HP', 20, 15000, "КИТАЙ", 2013)
print(sklad.reception())
