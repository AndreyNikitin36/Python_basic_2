class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки!")


class Pen:
    def draw(self):
        print("Pen")


class Pencil:
    def draw(self):
        print("Pencil")


class Handle:
    def draw(self):
        print("Handle")


a = Stationery("Pen")
a.draw()

b = Pen()
b.draw()

c = Pencil()
c.draw()

d = Handle()
d.draw()
