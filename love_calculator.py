print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")

combined_names = str(name1) + str(name2)

names = combined_names.lower()
one = names.count("t") +names.count("r")+ names.count("u")+ names.count("e")
two = names.count("l") + names.count("o") + names.count("v") +names.count("e")

result = str(one)+ str(two)
result_number = int(result)

if (10 > result_number) or (result_number > 90):
    message = ", you go together like coke and mentos"
elif (40 < result_number < 50):
    message = ", you are alright together"
else:
  message = ""

print(f"Your score is {result}{message}.")