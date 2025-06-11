import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_letters = ''
for letter in range (0, nr_letters):
    new_letters += random.choice(letters)
print(new_letters)

new_symbols = ''
for symbol in range (0, nr_symbols):
    new_symbols += random.choice(symbols)

new_numbers = ''
for number in range (0, nr_numbers):
    new_numbers += random.choice(numbers)

password_joined = new_letters+new_symbols+new_numbers

password_list = list(password_joined)
random.shuffle(password_list)
randomized_password = ''.join(password_list)

print(f"Your randomized password is: {randomized_password}")