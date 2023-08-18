from helpers import clear
from art import logo

## Print Logo
print(logo)
print("Welcome to the secret auction program.")

## Initialize variables
isThereMoreBidders = True
bids = {}

## Loop process to get the bidders
while isThereMoreBidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    user_input = input("Are there any other bidders? Type 'yes' or any other key to exit'\n")
    if user_input == 'yes':
        clear()
    else:
        isThereMoreBidders = False

## Present result
highest_bid = 0
highest_bidder = ''
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")