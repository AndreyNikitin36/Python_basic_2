class Road:
    def __init__(self):
        self._length = "1000"
        self._width = "5"
        self._thickness = "1"

    def sq_result(self, length, width, thickness):
        m = 25
        result_total = (m * thickness * length * width) / 1000
        print(f"Общая потребность в асфальте составляет {result_total} тонн.")


a = int(input("Введите длину дороги в метрах: "))
b = int(input("Введите ширину дороги в метрах: "))
c = int(input("Введите толщину слоя асфальта в сантиметрах: "))
result = Road()
result.sq_result(a, b, c)

