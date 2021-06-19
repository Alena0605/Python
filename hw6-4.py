"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed} км')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Вы превышаете скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Вы превышаете скорость!')


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'blue', 'Toyota', False)
print(town_car.name, town_car.color, town_car.speed, town_car.is_police)

town_car.go()
town_car.turn('налево')
town_car.show_speed()
town_car.stop()

sport_car = SportCar(260, 'white with blue', 'Nissan Skyline', False)
print('\n' + sport_car.name, sport_car.color, sport_car.speed, sport_car.is_police)

sport_car.go()
sport_car.turn('направо')
sport_car.show_speed()
sport_car.stop()

work_car = WorkCar(50, 'black', 'Hyundai', False)
print('\n' + work_car.name, work_car.color, work_car.speed, work_car.is_police)

work_car.go()
work_car.turn('налево, направо')
work_car.show_speed()
work_car.stop()

police_car = PoliceCar(80, 'white', 'Ford', True)
print('\n' + police_car.name, police_car.color, police_car.speed, police_car.is_police)

police_car.go()
police_car.turn('налево')
police_car.show_speed()
police_car.stop()
