#lesson4 task1
#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
#платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
#Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
#Учесть, что какие-то параметры будут отсутствовать.
from sys import argv

script_name, work_clock, money_clock, prize = argv

def zp (script_name, work_clock, money_clock, prize):
    try:
        work_clock_1 = float(work_clock)
        money_clock_1 = float(money_clock)
        prize_1 = float(prize)
        print("Имя скрипта: ", script_name)
        print("выработка в часах: ", work_clock)
        print("тавка в час: ", money_clock)
        print("премия: ", prize)
        if (work_clock_1 > 0 and money_clock_1 > 0) and prize_1 >=0:
            return print(f'Заработная плата сотрудника: {(work_clock_1*money_clock_1)+prize_1}')
    except ValueError:
        return print(f'ValueError. Вы не ввели численное значение или оно отрицательное, что не соотвецыует условию.')

zp(script_name, work_clock, money_clock, prize)

