result = 0
first_list = []
finish = ''

def my_calc(first_list):
    global result, finish
    new_result = 0
    for i in first_list:
        if i.upper() != 'Q':
            a = (i)
            new_result = int(a) + new_result
        else:
            finish = 'Q'
            break
    result = new_result + result
    first_list.clear()
    return f"{new_result} ({result})"


while finish != 'Q':
    first_list = input("Введите через пробел любые числа, для выхода нажмите 'Q': ").upper().split()
    print(my_calc(first_list))

