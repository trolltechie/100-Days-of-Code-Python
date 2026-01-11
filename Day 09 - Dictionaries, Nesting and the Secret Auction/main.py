from art import logo
print(logo)

# Function to find the highest bidder. First initialize empty string variable for names and integer variable for highest bid. Setting FOR loop to go through 
# each bidder in the bidding dictionary. Inside loop, set bid amount variable to the value of each bidder in the dictionary. If bid amount is greater than highest 
# bid, then set highest bid to bid amount and winner to bidder. After loop ends, print the winner and highest bid.

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Main code block. Initialize empty dictionary to store bids. Set boolean variable to control while loop. While loop to continue asking for bids until there are 
# no more bidders.Inside loop, ask for bidder's name and bid amount, storing them in the bids dictionary. Then ask if there are more bidders. 
# If no, set continue_bidding to False and call function to find highest bidder.

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)