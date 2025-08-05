from art import logo

print(logo)
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

def calculator():
    num1 = int(input("What is the first number?: "))
    for symbol in operaions:
        print(symbol)
    continue_calculating = True

    while continue_calculating:
        operation_symbol = input("What operation?: ")
        num2 = int(input("What is the next number?: "))
        calculation = operaions[operation_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continuation = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation ")

        if continuation == "y":
            num1 = answer
        else:
            print("Goodbye!")
            continue_calculating = False
            calculator()
calculator()