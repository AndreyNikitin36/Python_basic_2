import json

firm_dict = {}
firm_title = []
total_list = []
average_dict = {}
average = 0
i = 0

with open(r"Text_7.txt", "r", encoding="UTF-8") as firm_list:
    for line in firm_list:
        a = line.split(" ")
        firm_title.append(a[0])
        b = int(a[2]) - int(a[3])
        firm_title.append(b)
        if b > 0:
            average = average + b
            i += 1
    average_s = average / i
    l = len(firm_title)
    i = 0
    while i <= l - 1:
        key = firm_title[i]
        i += 1
        value = firm_title[i]
        new_dict = {key: value}
        firm_dict.update(new_dict)
        i += 1
    new_dict = {"average_profit": average_s}
    average_dict.update(new_dict)
    total_list.append(firm_dict)
    total_list.append(average_dict)
    print(total_list)
    print(f"Средняя прибыль компании составляет: {average_s}")

with open(r"Text_7.json", "a", encoding="UTF-8") as write_f:
    json.dump(total_list, write_f)
    

