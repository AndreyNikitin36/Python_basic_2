from itertools import count
from itertools import cycle

print("Функция 'count':")
num = int(input("Введите любое целое число: "))
my_list = []
for i in count(num):
    if i > num + 10:
        break
    else:
        my_list.append(i)
        print(i)

print("Функция 'cycle':")
c = 0
for i in cycle(my_list):
    if c > len(my_list) - 1:
        break
    print(i)
    c += 1
