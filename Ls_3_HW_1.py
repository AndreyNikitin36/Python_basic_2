def my_del(num_1, num_2):
    result = round(num_1 / num_2, 2)
    return result


print("Узнайте результат деления двух чисел!")

a, b = input("Введите первой число: "), input("Введите второе число: ")

try:
    a = int(a)
    b = int(b)
    a / b == 0
except (TypeError, ValueError):
    print("Ошибка! Вы ввели не числовое значение!")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")

print(my_del(a, b))
