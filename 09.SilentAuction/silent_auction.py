bids = {}
art = r'''⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡟⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠏⠀⠀⠀⢀⣾⢿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠀⠀⠀⢠⡿⠃⠀⠉⠛⠿⣧⣀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠃⠀⠀⠀⣠⡿⠁⠀⠀⠀⠀⠀⠈⠙⠻⣶⣄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠁⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⡀⢀⣼⣏⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⡟⠀⠈⠙⢿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠟⠀⠀⠀⢠⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⠙⠻⣦⣄⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⢠⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠷⣦⣄⠉⣻⣶⣤⣀⠀⢀⣾⠃⠀⠀⠀⣠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⣰⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠁⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣤⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿'''

def clear_screen():
    print("\n" * 100)

def find_highest_bid(bids_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bids_dictionary:
        bid_amount = bids_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\nHighest bidder is: {winner} with a bid of ${highest_bid}")

print(art)
print('Welcome to the Auction Game!')

continue_bidding = True
while continue_bidding:
    contestants_name = input("Enter bidder's name: ")
    while True:
        try:
            bidding_money = int(input('How much money would you like to bid?: $'))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    bids[contestants_name] = bidding_money
    print("Are there any other bidders? Type 'yes' or 'no'.")
    more_bidders = input().lower()

    if more_bidders == 'yes':
        clear_screen()
    else:
        continue_bidding = False
        clear_screen()
        find_highest_bid(bids)
