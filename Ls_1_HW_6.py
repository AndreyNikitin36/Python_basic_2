day = 1
a = float(input('Введите ваш результат пробежки за первый день в км: '))
b = float(input('Введите вашу цель по ежедневной пробежке в км: '))
print(f"{day}-день, ваш результат {a} км")

while a < b:
    distance = a * 1.10
    a = distance
    day += 1
    print(f"{day}-день, ваш результат {a:.2f} км")

print(f"Вы достигнете своей цели на {day} день, пробежав {a:.2f} км, что больше вашей цели {b} км.")
