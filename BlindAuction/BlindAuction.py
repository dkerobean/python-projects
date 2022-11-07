from replit import clear

bids = {}
bidding_finished = False


def find_winner(bid_record):
    winning_bid = 0
    winner = ""
#finding winner based on bid ammount
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > winning_bid:
            winning_bid = bid_amount
        winner = bidder

    print(f"The winner of this bid is {winner} with an amount of ${winning_bid}")


while not bidding_finished:
    name = input("What is your name: \n")
    price = int(input("What is your bid ?:  $ "))
    bids[name] = price
    bid_status = input("Are there any other bids? (Yes/No) ")
    if bid_status.upper() == "NO":
        bidding_finished = True
        find_winner(bids)
    elif bid_status.upper() == "YES":
        clear()








