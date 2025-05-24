height = float(input("your height in meters?"))
weight = int(input("your weight in kg?"))


BMI = weight/(height**2)

if BMI < 18.5:
    message = "you are underweight."
elif  18.5 <= BMI < 25:
    message = "you have a normal weight."
elif 25 <= BMI <  30:
    message = "you are slightly overweight."
elif 30 <= BMI <  35:
    message = "you are obese."
else: # 35 <= BMI
    message = "you are clinically obese."

print(f"Your BMI is {BMI}, {message}")