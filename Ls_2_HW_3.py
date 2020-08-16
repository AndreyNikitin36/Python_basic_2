# Решение через словарь

m_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}

month = int(input('Введите любой номер месяца в году (от 1 до 12): '))

print(m_dict.get(month))

# Решение через списки

season_list = ['Зима', 'Весна', 'Лето', 'Осень']
month_list = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

month = int(input('Введите любой номер месяца в году (от 1 до 12): '))
a = month_list.index(month)

if 2 < a < 6:
    print(season_list[1])

elif 5 < a < 9:
    print(season_list[2])

elif 8 < a < 12:
    print(season_list[3])

else:
    print(season_list[0])

