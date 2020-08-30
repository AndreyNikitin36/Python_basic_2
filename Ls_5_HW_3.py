with open(r"Text_3.txt", "r", encoding="UTF-8") as check:
    content = check.read()
    print(f"Полный список сотрудников:\n{content}")

print("Список сотрудников с окладом менее 20 000 руб.: ")
salary_list = []
i = 0
with open(r"Text_3.txt", "r", encoding="UTF-8") as check:
    for line in check:
        str_wrd = line.split(" ")
        salary = float(str_wrd[1][:-1])
        str_wrd.pop(1)
        str_wrd.append(salary)
        salary_list.append(salary)
        i += 1
        if str_wrd[1] < 20000:
            print(f"{str_wrd[0]} {str_wrd[1]}")

average_salary = sum(salary_list) / i
print(f"Средняя величина дохода всех сотрудников равна {int(average_salary)}")