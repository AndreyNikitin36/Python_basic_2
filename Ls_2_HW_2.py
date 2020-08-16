my_list = input('Введите несколько значений (числа, слова) через запятую для формирования списка: ')

my_list = list(my_list.split(","))

print(my_list)

length = len(my_list) - 2

i = 0

while i <= length:
    a = my_list[i]
    b = my_list[i + 1]
    a, b = b, a
    my_list.pop(i)
    my_list.insert(i, a)
    my_list.pop(i + 1)
    my_list.insert(i + 1, b)
    i += 2

print(my_list)
