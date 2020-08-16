my_list = input("Напечатайте, пожалуйста, несколько слов или предложение: ")

my_list = my_list.split(" ")
a = None

for ind, el in enumerate(my_list, 1):
    a = str(el)
    el = a[:10]
    print(ind, el)

