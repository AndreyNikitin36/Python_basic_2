num_product = 1
goods_list = []
finish_in = 'да'

while finish_in != 'н':
    name_product = input(f"Введите название товара № {num_product}: ")
    name_product = name_product.title()
    price_product = input(f"Введите цену товара № {num_product}: ")
    quantity_product = input(f"Введите количество товара № {num_product}: ")
    unit_product = input(f"Введите единицы измерения товара № {num_product}: ")
    product_dict = {'Название': name_product, 'Цена': price_product, 'Количество': quantity_product, 'Ед.изм.': unit_product}
    product_t = (num_product, product_dict)
    goods_list.append(product_t)
    finish_in = input("Нажмите клавишу Enter для продолжения ввода товаров или нажмите клавишу 'н', чтобы закончить ввод: ")
    num_product += 1

print(goods_list)
"\t"
# Теперь соберем аналитику
value_1 = []
value_2 = []
value_3 = []
value_4 = []

for i in goods_list:
    a = goods_list.index(i)
    get_dict = list(goods_list[a])
    get_dict = get_dict[1]
    get_keys = list(get_dict.keys())
    get_values = list(get_dict.values())
    key_1 = get_keys[0]
    key_2 = get_keys[1]
    key_3 = get_keys[2]
    key_4 = get_keys[3]
    value_1.append(get_values[0])
    value_2.append(get_values[1])
    value_3.append(get_values[2])
    value_4.append(get_values[3])

value_1 = list(set(value_1))
value_2 = list(set(value_2))
value_3 = list(set(value_3))
value_4 = list(set(value_4))

new_dict = {key_1: value_1, key_2: value_2, key_3: value_3, key_4: value_4}
"\t"
print(new_dict)

