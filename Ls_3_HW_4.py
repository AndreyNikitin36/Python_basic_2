def my_func(x, y):
    result = x ** y
    print(f"Первый способ: {round(result, 4)}")
    if y == -1:
        result_2 = 1 / x
    elif y == 0:
        result_2 = 1
    else:
        i = 2
        y = abs(y)
        c = x * x
        while i != y:
            c = c * x
            i += 1

        result_2 = 1 / c
    return f"Второй способ: {round(result_2, 4)}"


a = int(input("Введите целое положительное число: "))
b = int(input("Введите целое отрицательное число: "))

print(my_func(a, b))
