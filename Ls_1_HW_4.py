number = int(input('Введите любое целое число больше 0: '))
great_num = 0

while number < 0:
    print('Введено отрицательное число. Попробуйте еще раз.')
    number = int(input('Введите целое положительное число: '))

n = number
while n > 0:
    big_num = n % 10
    n = n // 10
    if big_num > great_num:
        great_num = big_num

    elif big_num == 9:
        break

print(f"Наибольшей цифрой в вашем числе {number} является цифра {great_num}")
