from time import sleep
from termcolor import colored


class TrafficLight:
    def __init__(self):
        print("Включаем светофор!")
        self.__color = ""

    def running(self):
        while True:
            color = "Красный"
            print(colored(color, 'red', attrs=["bold"]))
            sleep(7)
            color = "Желтый"
            print(colored(color, "yellow", attrs=['underline']))
            sleep(2)
            color = "Зеленый"
            print(colored(color, "green", attrs=["bold"]))
            sleep(7)
            color = "Желтый"
            print(colored(color, "yellow", attrs=['underline']))
            sleep(2)

result = TrafficLight()
result.running()
