def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    a = min(my_list)
    my_list.remove(a)
    result = sum(my_list)
    return result


num_1, num_2, num_3 = int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(
    input("Введите третье число: "))

print(my_func(num_1, num_2, num_3))
