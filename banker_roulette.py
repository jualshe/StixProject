import random

names_string = input ("Give me everybody's names separated by a comma!\n")
#Angela, Ben, Jenny, Michael, Chloe
names = names_string.split(",")
print(names)
random_name = random.sample(names, 1)[0]

print(f"{random_name} is going to buy the meal today!")


