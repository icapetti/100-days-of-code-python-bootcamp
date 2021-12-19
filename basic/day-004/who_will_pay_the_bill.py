import random

names = input("Enter names separated by commas: ").split(", ")
name_to_pay = random.randint(0, len(names)-1)

print(f"{names[name_to_pay]} is going to buy the meal today!")