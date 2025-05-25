print ("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >=120:
    print ("You can ride the rollercoaster!")
    age = int(input("how old are you? "))

    if age <12:
        print("your ticket is $5")
    elif age <= 18:
        print("you tiket is $7")
    else:
        print("your ticket is $12")
else:
    print("come when you grow up higher!")

