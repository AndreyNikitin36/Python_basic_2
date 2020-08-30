with open(r"Text_2.txt", "r", encoding="UTF-8") as my_person:
    my_list = my_person.readlines()
    number = len(my_list)
    print(f"Файл содержит {number} стр.")

str_num = 1
str_wrd = []
with open(r"Text_2.txt", "r", encoding="UTF-8") as my_person:
    for line in my_person:
        str_wrd = line.split(" ")
        print(f"В {str_num} строке {len(str_wrd)} слов.")
        str_num += 1



