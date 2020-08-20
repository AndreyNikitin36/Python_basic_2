def my_data(name, family, date_birthday, city, mail, mobile):
    print(f"Ваше имя: {name}, фамилия: {family}, год рождения: {date_birthday}, город проживания: {city}, почта: {mail}, телефон: {mobile}")

name, family, date_birthday, city, mail, mobile = input("Введите через пробел ваше имя, фамилию, год рождения, город проживания, адрес электронной почты и номер телефона:\n").split()

my_data(name, family, date_birthday, city, mail, mobile)

