print('''__________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|''')

print("Welcome to Treasure Island\n"
      "Your mission is to find the treasure")

first = input("You are at a cross road type left or right?")
if first == "right":
      print("Fall into a hole. Game Over.")
else:
      second = input("swim or wait?")
      if second == "swim":
            print("Attacked by trout. Game Over.")
      else:
            third = input("which door? red or blue or yellow")
            if third == "blue" :
                  print("bye bye")
            if third == "red":
                  print("oh well you lost")
            else:
                  print("YOU WOOOOON!!")