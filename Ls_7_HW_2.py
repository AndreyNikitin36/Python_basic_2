from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def size_cloth(self):
        pass

    def __add__(self, other):
        return f"Общий расход ткани составит {round(self.size_cloth + other.size_cloth, 2)} метров."


class Coat(Clothes):
    @property
    def size_cloth(self):
        v_coat = (self.size / 6.5) + 0.5
        v_coat = round(v_coat, 2)
        print(f"Расход ткани на пальто составит {v_coat} метров.")
        return v_coat


class Suit(Clothes):
    @property
    def size_cloth(self):
        h_suit = (2 * self.size) + 0.3
        h_suit = round((h_suit / 100), 2)
        print(f"Расход ткани на костюм составит {h_suit} метров.")
        return h_suit


v = int(input("Введите свой размер для пальто: "))
h = int(input("Введите свой рост в см для костюма: "))

coat = Coat(v)

suit = Suit(h)

print(coat + suit)
