class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return self.num

    def __add__(self, other):
        result = self.num + other.num
        print(result)

    def __sub__(self, other):
        if self.num - other.num > 0:
            result = self.num - other.num
            print(result)
        else:
            print("Нельзя вычесть!")

    def __mul__(self, other):
        result = self.num * other.num
        print(result)

    def __floordiv__(self, other):
        result = self.num // other.num
        print(result)

    def make_order(self, quantity):
        return "\n".join(['*' * quantity for _ in range(self.num // quantity)]) + "\n" + "*" * (self.num % quantity)


a = Cell(20)
b = Cell(15)
c = a + b
c = a - b
c = a * b
c = a // b
print(a.make_order(5))
