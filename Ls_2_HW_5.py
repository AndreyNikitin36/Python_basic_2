my_list = [8, 4]

print(f"Исходный рейтинг: {my_list}")

while True:
    new_num = int(input('Введите любое натуральное число: '))

    for i in my_list:
        if i == new_num:
            my_list.insert(my_list.index(i), new_num)
            break

    if new_num > my_list[0]:
        my_list.insert(0, new_num)

    elif new_num < my_list[-1]:
        my_list.append(new_num)

    elif new_num != my_list[0] & my_list[-1]:
        for i in my_list:
            a = my_list.index(i)
            b = my_list.count(i)
            if new_num == my_list[a] - 1:
                my_list.insert(a + b, new_num)
                break
            elif new_num == my_list[a] + 1:
                my_list.insert(a, new_num)
                break
            elif my_list[a + 1] < new_num < my_list[a]:
                my_list.insert(a + 1, new_num)
                break

    print(f"Текущий рейтинг {my_list}")

