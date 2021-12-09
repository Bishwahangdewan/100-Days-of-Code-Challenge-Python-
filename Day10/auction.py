print("WELCOME TO AUCTION")

bids = []
flag = True


def store_bid(name, bid):
    each_bid = {"name": name, "bid": bid}

    bids.append(each_bid)


def ask():
    name = input("What is your name?\n ")
    bid = int(input("How much do you want to bid? \n"))

    store_bid(name, bid)


def calculate_bid(bids):
    highest_bid = 0
    bidder_name = ''
    for dictionary in bids:
        if dictionary["bid"] > highest_bid:
            highest_bid = dictionary["bid"]
            bidder_name = dictionary["name"]

    print(f"The highest bid is {highest_bid} and the bidder is {bidder_name}")



while flag:
    ask()
    go_on = input("Do you wish to continue? Type 'yes' or 'no'\n ")

    if go_on == "yes":
        flag = True
    else:
        flag = False
        calculate_bid(bids)
