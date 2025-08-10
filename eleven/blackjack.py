import random
from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# wannaplay = input("Do you want to play blackjack? Type 'yay' or 'nay': " )

#TODO 2: Deal both user and computer a starting hand of 2 random card values.
user_cards = random.sample(cards, 2)
print(user_cards)
computer_cards = random.sample(cards,2)
print(f'[{computer_cards[0]}], [X]')

#TODO 3:Detect when computer or user has a blackjack. (Ace + 10 value card).

if sum(computer_cards) == 21:
    print("Computer won!")
elif sum(user_cards) == 21:
    print("User won!")

#TODO: If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
if sum(user_cards) or sum(computer_cards) > 21:
    if 11 in user_cards:
        11 == 1

#TODO 5:
# more_card = input("Type 'yay' if you want another card  or 'nay' to pass: ")


#Your final hand: [x,x]
#Computer's final hand: [y,y]'
# WHO wins?

#wannaplay = input("Do you want to play blackjack? Type 'yay' or 'nay': " )

#The Ace can count as 11 or 1.
