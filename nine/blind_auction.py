from art import logo
print(logo)
print("Welcome to the secret auction program.")

# TODO-1: Ask the user for input
name = input("What is your name?\n")
bid = input("What is your bid?\n")

# TODO-2: Save data into dictionary {name: price}
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


