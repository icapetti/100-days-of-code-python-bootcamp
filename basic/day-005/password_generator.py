import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

symbols = ['@', '*', '%', '&', '#', '/', '+', '-', '!', '$', '?', '_']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
letters_qty = int(input("How many letters would you like in your password? "))
symbols_qty = int(input("How many symbols would you like in your password? "))
numbers_qty = int(input("How many numbers would you like in your password? "))

password = []
for i in range(0, letters_qty):
    password.append(random.choice(letters))

for i in range(0, symbols_qty):
    password.append(random.choice(symbols))

for i in range(0, numbers_qty):
    password.append(random.choice(numbers))

random.shuffle(password)
password = ''.join(password)
print(f"Here is your password: {password}")
