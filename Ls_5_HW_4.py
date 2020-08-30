alphabet = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
i = 0
with open(r"Text_4.txt", "r+", encoding="UTF-8") as change:
    for line in change:
        str_wrd = line.split(" ")
        key = str_wrd[0]
        str_wrd[0] = alphabet.get(key)
        line = str_wrd
        i += 1
        print(f"{str_wrd[0]} {str_wrd[1]} {str_wrd[2]}")
        if i == 0:
            with open(r"Text_4_1.txt", "x", encoding="UTF-8") as new_list:
                new_list.writelines(line)
        else:
            with open(r"Text_4_1.txt", "a", encoding="UTF-8") as new_list:
                new_list.writelines(line)

