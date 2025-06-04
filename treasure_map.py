line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot. A,B,C and 1,2,3")

position = input() # Where do you want to put the treasure?

x_axis  = position[0].lower()
if x_axis == "a":
    x_axis = 0
elif x_axis == "b":
    x_axis = 1
else:
    x_axis = 2

y_axis = int(position[1])

# another option
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
#map[number_index][letter_index] = "X"

map[y_axis-1] [x_axis] = "X"

print(f"{line1}\n{line2}\n{line3}")