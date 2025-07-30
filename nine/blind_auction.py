from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")

# TODO-1: Ask the user for input
name = input("What is your name?\n")
bid = input("What is your bid?\n")

# TODO-2: Save data into dictionary {name: price}
bidders = []
def add_new_bidders (person, price):
    new_bidder = {
        "name": person,
        "bid": price
    }
    bidders.append(new_bidder)

add_new_bidders(person=name, price=bid)


print(bidders)
# TODO-3: Whether if new bids need to be added
additional_user = input("Are there more bidders? Yes/No?\n")
if additional_user == "Yes".lower():
    clear()
    add_new_bidders(person=name, price=bid)

else:
    print("quit")
    quit()

# TODO-4: Compare bids in dictionary


