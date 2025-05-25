height = float(input("your height in meters?"))
weight = int(input("your weight in kg?"))


BMI = round(weight/(height**2))
print (BMI)

if BMI < 18.5:
    message = "you are underweight."
elif BMI < 25:
    message = "you have a normal weight."
elif BMI <  30:
    message = "you are slightly overweight."
elif BMI <  35:
    message = "you are obese."
else: # 35 <= BMI
    message = "you are clinically obese."

print(f"Your BMI is {BMI}, {message}")