
#add
def add (n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply (n1, n2):
    return  n1 * n2

#divide
def divide (n1, n2):
    return n1 / n2


operaions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

for each in operaions:
    print(each)