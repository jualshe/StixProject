height = input ("your height in meters?")
weight = input ("your weight in kg?")

new_weight = int(weight)
new_height = float(height)
BMI = round((new_weight/(new_height**2)),5)
print(BMI)
if BMI >18 < 25:
    print("you are in healthy range")
else:
    print("you need to work on your diet")