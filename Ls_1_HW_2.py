number = int(input('Введите любое количество секунд: '))
while number < 0:
    print('Число должно должно быть больше 0. Введите количество секунд еще раз, будьте внимательнее!: ')
    number = int(input('Введите любое количество секунд: '))

hour = number // 3600
minute = number // 60 - hour * 60
seconds  = number % 60
print(f"ч:м:с - {hour:02}:{minute:02}:{seconds:02}")



