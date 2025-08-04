
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

for symbol in operaions:
    print(symbol)
operation_symbol = input("What operation from the list?: ")

num2 = int(input("What is the second number?: "))

calculation = operaions[operation_symbol]
answer = calculation(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")