n = input('Введите любое число больше 0: ')

while n < '0':
    print('Будьте внимательнее, надо ввести число больше 0!')
    n = input('Попробуйте еще раз: ')

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

