print ("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >=120:
    print ("You can ride the rollercoaster!")
    age = int(input("how old are you? "))
    total = 0
    if age <12:
        total = 5
        print("Child tickets are $5")

    elif age <= 18:
        total = 7
        print("Youth tickets are $7")
    elif age>=45 and age <= 55:
        print("Ride is free on us!")
    else:
        total = 12
        print("Adult tickets are $12")

    photos = input("Do you want photos? Type Y or N.")
    if photos == 'Y':
        total += 3
    print(f"Your final bill is ${total}")
    # else:
    #     print(f"Total bill is ${total}?")

else:
    print("come when you grow up higher!")

