from art import logo

print(logo)


def get_the_winner(players):
    winner_amount = 0
    winner_player = ""
    for player in players:
        bids_amount = int(players[player])
        if bids_amount >= winner_amount:
            winner_amount = bids_amount
            winner_player = player
    print("------------------------------")
    print(f"The winner is {winner_player}, with a bid value ${winner_amount}.")


players = {}
auction_quit = False
while not auction_quit:
    name = input("What is you name?:  ")
    bid = input("What's your bid?: $")
    players[name] = bid
    other_bidders = input("Are there any other Bidders? Type 'yes' or 'no' ").lower()
    if other_bidders == "yes":
        for _ in range(100):
            print("|")
    elif other_bidders == "no":
        auction_quit = True
        get_the_winner(players)
    else:
        print("Invalid Input\n-----------------------")

