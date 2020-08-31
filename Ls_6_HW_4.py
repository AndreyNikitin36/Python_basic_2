class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль: {self.color} {self.name}, начал движение!")

    def stop(self):
        print(f"Автомобиль: {self.color} {self.name}, остановился!")

    def turn(self, direction):
        print(f"Автомобиль: {self.color} {self.name}, повернул {direction}!")

    def show_speed(self):
        print(f"Скорость автомобиля составляет: {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Автомобиль:{self.color} {self.name} превысил скорость 60 км/ч")
        else:
            print(super(TownCar, self).show_speed())


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Автомобиль:{self.color} {self.name} превысил скорость 60 км/ч")
        else:
            print(super(TownCar, self).show_speed())


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.is_police == True:
            print(f"Полиции все можно!")
        else:
            print("Это не полиция!")


a = Car(60, "Красный", "Лада")

b = TownCar(56, "Зеленый", "Камаро")
print(b.go())
print(b.turn("Налево"))
print(b.show_speed())

c = SportCar(100, "Желтый", "Инфинити")
print(c.go())
print(c.turn("Вокруг"))
print(c.show_speed())

d = WorkCar(80, "Черный", "Камаз")

print(d.go())
print(d.turn("Направо"))
print(d.show_speed())

e = PoliceCar(150, "Белый", "Лимузин", 1)

print(e.go())
print(e.turn("Назад"))
print(e.show_speed())

