from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
bidders = []
print(bidders)
def add_new_bidders (person, price):
    new_bidder = {
        "name": person,
        "bid": price
    }
    bidders.append(new_bidder)
    print(bidders)
def higher_bidder():
    highest_bid = 0
    winner=""
    for name, bid in bidders.items:
        if bid > highest_bid:
            highest_bid = bid
            winner = name
            print(f"The winner is {winner} with the highest bid of ${bid}.congrats!")

# TODO-3: Whether if new bids need to be added
more_users = True
while more_users:
    name = input("What is your name?\n")
    bid = input("What is your bid?\n")
    add_new_bidders(person=name, price=bid)

    clear()
    more_users = input("Are there more bidders? Yes/No?\n").lower()
    if more_users == "no":
        print("no, ok, goodbye!")
        more_users = False
# TODO-4: Compare bids in dictionary


