class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f"{position}: {name} {surname}")


    def get_total_income(self):
        result = int(worker._income.get("wage")) + int(worker._income.get("bonus"))
        print(f"Ваш доход: {result}")


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
position = input("Введите должность: ")
wage = input("Оклад работника: ")
bonus = input("Премия работника: ")
worker = Position(name, surname, position, wage, bonus)
print(worker.name)
print(worker.surname)
print(worker.position)
print(worker._income)
print()

worker.get_full_name()
worker.get_total_income()

