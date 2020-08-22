from math import factorial

n = int(input("Введите любое целое число: "))


def fact(n):
    for i in range(1, n + 1):
        yield i


for el in fact(n):
    print(f"Факториал числа {el}! равен {factorial(el)}")
