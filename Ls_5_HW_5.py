from random import randint
i = 0
gen_list = []
sum_list = []
total_sum = None
with open(r"Text_5.txt", "w+", encoding="UTF-8") as num_list:
    gen_list.append(randint(-1000, 1000))
    sum_list.append(gen_list[i])
    total_sum = sum(sum_list)
    gen_list[i] = str(gen_list[i])
    gen_list[i] = gen_list[i] + " "
    num_list.write(gen_list[i])
    i = 1


with open(r"Text_5.txt", "a+", encoding="UTF-8") as num_list:
    while i <=9:
        gen_list.append(randint(-1000, 1000))
        sum_list.append(gen_list[i])
        total_sum = sum(sum_list)
        gen_list[i] = str(gen_list[i])
        gen_list[i] = gen_list[i] + " "
        num_list.writelines(gen_list[i])
        i += 1

with open(r"Text_5.txt", "r", encoding="UTF-8") as num_list:
    print(f"Содержимое файла: {num_list.read()}")

print(f"Сумма чисел в файле: {total_sum}")
