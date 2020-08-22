from random import randint
start_list = []

i = 0
while i < 20:
    start_list.append(randint(0, 100))
    i += 1

print(f"Исходный список: {start_list}")

new_list = [i for i in start_list if start_list[start_list.index(i) - 1] < i]

new_list.pop(0)

print(f"Новый список: {new_list}")

