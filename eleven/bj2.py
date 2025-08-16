import random
from art import logo

print(logo)
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
# 11 is the Ace.

user_cards = []
computer_cards = []
is_game_over = False




for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
    """take a list of cards and return the scode calculated from the cards"""
    #'0'' is blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #if ace(11) after 21 - make it '1'
    if 11  in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if user_score == 0 or computer_score ==0 or user_score > 21:
    is_game_over = True
