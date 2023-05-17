import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '-', '+']

print("Welcome To Password Generator")

letter = 8
number = 4
symbol = 2
password_list = []
for i in range(1, letter + 1):
    password_list.append(random.choice(letters))

for i in range(1, number + 1):
    password_list.append(random.choice(numbers))

for i in range(1, symbol + 1):
    password_list.append(random.choice(symbols))

password = ""
random.shuffle(password_list)
for i in password_list:
    password += i

print(password)
