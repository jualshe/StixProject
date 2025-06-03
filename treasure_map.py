line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
user_input = position.split(",")
print(user_input)

coordinates = len(user_input)
print(coordinates)

coordinates_row = coordinates[0]
coordinates_column = coordinates[1]





print(f"{line1}\n{line2}\n{line3}")