# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
class Road:
    def __init__(self, _length, _width):
        self._length = _length #атрибуты сделать защищенными
        self._width = _width

    def Rectangle(self):
        return (self._length * self._width)



class MassCount(Road):
    def __init__(self,_length, _width, weigth, tickness):
        super().__init__(_length, _width) #Чтобы ботать с унаследованными атрибутами, нужно их перечислить
        self.weigth = weigth
        self.tickness = tickness
        intake = self._length * self._width * self.weigth * self.tickness / 1000
        print(intake)

r = Road(20, 5000)
print(f'Площадь: {r.Rectangle()} м2')
print(f'Масса асфальтп для {r.Rectangle()} м2 = ')
MassCount(20, 5000, 25, 5)
