import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = input("choose and type - rock, paper or scissors?\n").lower()

#when user enters a choice - print user's choice
print(f"Your choice is {user_choice}!")
if user_choice == "rock":
    print(rock)
elif user_choice == "paper":
    print(paper)
elif user_choice == "scissors":
    print(scissors)
else:
    print("What was that? Try again! \n")


# randomly choose the computer option - rock, paper or scissors

RPS_list = ["rock", "paper", "scissors"]
random_RPS = random.choice(RPS_list)
print(f"Your opponent's choice is {random_RPS}!")

if random_RPS == "rock":
    print(rock)
elif random_RPS == "paper":
    print(paper)
else:
    print(scissors)

# compare using the rules and print the results
if user_choice == random_RPS:
    print("Tight game! Try again!")

# Rock wins against scissors.
elif user_choice == "rock" and random_RPS == "scissors":
    print("Good try! You won!")
elif user_choice == "scissors" and random_RPS == "rock":
    print("Nah! Try again!")

# Scissors win against paper.
elif user_choice == "scissors" and random_RPS == "paper":
    print("Good try! You won!")
elif user_choice == "paper" and random_RPS == "scissors":
    print("Try again, you lost!")

# Paper wins against rock.
elif user_choice == "paper" and random_RPS == "rock":
    print("Good try! You won!")
elif user_choice == "rock" and random_RPS == "paper":
    print("Try again, you lost!")
else:
    print("Try again!")