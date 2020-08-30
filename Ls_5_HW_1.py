with open(r"Text_1.txt", "w", encoding="UTF-8") as my_file:
    my_list = input("Введите любые символы и нажмите Enter: ")
    my_file.write(my_list)
    my_file.write("\n")


while True:
    if my_list != "":
        my_list = input("Введите любые символы и нажмите Enter: ")
        with open(r"Text_1.txt", "a", encoding="UTF-8") as my_file:
            my_file.write(my_list)
            my_file.write("\n")
    else:
        with open(r"Text_1.txt", "r", encoding="UTF-8") as my_file:
            content = my_file.read()
            print(f"Содержимое файла:\n{content}")
            break



