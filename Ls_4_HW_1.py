from sys import argv

script_name, productivity, rate, prize = argv

wages = (int(productivity) * int(rate)) + int(prize)

print(f"Ваша заработная плата составит {wages} рублей")

