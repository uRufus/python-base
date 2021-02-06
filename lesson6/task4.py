'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    current_speed = 0

    def __init__(self, speed, color, name, is_police=bool(0)):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")
        self.current_speed = self.speed

    def stop(self):
        print(f"Машина {self.name} остановилась")
        self.current_speed = 0

    def turn(self, direction):
        print(f"Машина {self.name} повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость  машины {self.name} составляет {self.current_speed} км/ч.")


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        if self.current_speed > self.speed_limit:
            return print(f"Максимальная разрешенная скорость 60 км/ч. "
                         f"Вы превысили скорость на {self.current_speed - self.speed_limit} км/ч.")
        print(f"Текущая скорость  машины {self.name} составляет {self.current_speed} км/ч.")


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if self.current_speed > self.speed_limit:
            return print(f"Максимальная разрешенная скорость 60 км/ч. "
                         f"Вы превысили скорость на {self.current_speed - self.speed_limit} км/ч.")
        print(f"Текущая скорость  машины {self.name} составляет {self.current_speed} км/ч.")


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


town_car = TownCar(70, "Brown", "Mustang")
town_car.show_speed()
town_car.go()
town_car.turn("Север")
town_car.show_speed()

work_car = WorkCar(50, "Black", "Камаз")
work_car.show_speed()
work_car.go()
work_car.turn("Юг")
work_car.show_speed()

sport_car = SportCar(130, "Black", "Lamborghini")
sport_car.show_speed()
sport_car.go()
sport_car.turn("Восток")
sport_car.show_speed()

police_car = PoliceCar(130, "Black", "Lamborghini Diablo")
police_car.show_speed()
police_car.go()
police_car.turn("Запад")
police_car.show_speed()
