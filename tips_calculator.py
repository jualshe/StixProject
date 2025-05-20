print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

before_tip = total/people
tip_amount = (tip_percentage/100)*before_tip
result = (float(before_tip)+float1(tip_amount))
result_rounded = round(result, 2)

message = f"Each person should pay {result} dollars"
print(message)
