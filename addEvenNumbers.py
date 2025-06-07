target = int(input("enter the number\n "))

total = 0
for number in range(0, target+1, 2):
    total += number
    #another option without specifying a step in a range
    # if number % 2 == 0:
    #     total += number
print(total)