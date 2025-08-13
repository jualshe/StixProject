import random

from art import logo
# print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#deal both user and computer a starting hand of 2 random card values.
user_cards = random.sample(cards, 2)
print(user_cards)
computer_cards = random.sample(cards,2)
print(f'[{computer_cards[0]}], [X]')

def comparison():
    if blackjack_check():
        return
    else:
        if user_total == computer_total:
            print("DRAW!")
            # return

        elif user_total < computer_total < 22:
            print("Computer winsooo!")
        elif want_more_card == False:
            print("User wins oo!")

# else:
    #     print("User wins oo!")

# is there a blackjack?
def blackjack_check():
    if computer_total == 21:
        print("Blackjack! Computer won!")
        return True
    elif user_total == 21:
        print("Blackjack! User won!")
        return True
    else:
        return False

want_more_card = True
while want_more_card:
    user_total = sum(user_cards)
    computer_total = sum(computer_cards)
    if blackjack_check():
        want_more_card = False
        break

    def adjust_for_ace(cards):
        while sum(cards) > 21 and 11 in cards:
            cards[cards.index(11)] = 1

    more_card = input("Type 'yes' if you want another card  or 'no' to pass: ")

    if more_card == "no":
        print("no more cards for the user ")
        want_more_card = False

        # computer plays
        while sum(computer_cards) <= 17:
            print("computer is drawing a card")
            computer_cards += random.sample(cards,1)
            adjust_for_ace(computer_cards)
            computer_total = sum(computer_cards)
            print(computer_cards)
            print(computer_total)
            blackjack_check()

            if computer_total > 21:
                want_more_card = False
                print("COMPUTER LOST!")
            else:
                comparison()
    else:
        user_cards += random.sample(cards, 1)
        adjust_for_ace(user_cards)
        user_total = sum(user_cards)
        blackjack_check()
        print("one more card dealt for the user")
        print(user_cards)
        print(user_total)
        if user_total > 21:
            want_more_card = False
            print("USER LOST!")
        else:
            comparison()

print(f'the score is user: {user_total} vs computer: {computer_total}')