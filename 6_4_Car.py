"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed} км/ч.')
        if self.speed > 60:
            print("Вы превысили скорость.")


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed} км/ч.')
        if self.speed > 40:
            print("Вы превысили скорость.")


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        Car.__init__(self, name, color, speed, is_police=True)


car_1 = Car("BMW", "черный", 100)
car_2 = TownCar("Audi", "серый", 70)
car_3 = WorkCar("Buick", "белый", 40)
car_4 = PoliceCar("Aston Martin", "красный", 150)
print(car_4.name)
print(car_3.color)
car_1.go()
car_2.stop()
car_3.turn("направо")
car_2.show_speed()
car_3.show_speed()
print("Это полицейская машина:", car_4.is_police)
