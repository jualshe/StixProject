print('''__________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|''')

print("Welcome to Treasure Island\n"
      "Your mission is to find the treasure.\n ")

first = input('You are at a cross road. Where are you going to go? Type "left" or "right"?\n').lower()
if first == "left":
      second = input('Do you choose "swim" or "wait"?\n').lower()
      if second == "wait":
            third = input("There are 3 doors in front of you and you need to choose one? red, blue or yellow?\n")
            if third == "blue":
                  print("bye bye, you've been eaten by beasts.")
            elif third == "red":
                  print("oh well.. you lost, you've been burned by fire.")
            elif third =="yellow":
                  print("You found the treasure! YOU WOOOOOONN!!!!")
            else:
                  print("Ypo chose the dooe that doesn't exist. Game over!")

      else:
            print("Oh no! You've been attacked by a trout. Game Over.")
else:
      print("You fall into a hole. Game Over.")