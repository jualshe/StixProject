import random

names_string = input ("Give me everybody's names separated by a comma!\n")
# Angela, Ben, Jenny, Michael, Chloe
names = names_string.split(",")
print(names)

# get the total number of items in the list
a = len(names)

random_name = random.randint(0,a-1)
person_who_will_pay= names[random_name]

print(f"{random_name} is going to buy the meal today!")