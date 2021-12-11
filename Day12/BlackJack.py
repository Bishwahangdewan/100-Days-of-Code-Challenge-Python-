# BlackJack Game

import random


# function to calculate the total
def calc_total(cards, whose_card):
    total = 0

    for card in cards:
        # check if cars is A
        if card == 'A':
            if whose_card == 'player':
                total += 11
            elif whose_card == 'dealer':
                if total <= 10:
                    total += 11
                else:
                    total += 1
        else:
            total += card

    return total


# function to check for Bust
def check_bust(cards, whose_card):
    total = calc_total(cards, whose_card)
    if total > 21:
        return True
    else:
        return False


# function for hit
def hit(p_cards):
    card = random.choice(cards);
    p_cards.append(card)
    print(f"Your new Card now is {p_cards}")


# get_result
def get_result(p_cards, d_cards):
    check_dealer_bust = check_bust(d_cards, 'dealer')

    if check_dealer_bust:
        print(f"Dealer {d_cards} exceeds 21")
        print("You Win")

    else:
        p_cards_total = calc_total(p_cards, 'player')
        d_cards_total = calc_total(d_cards, 'dealer')

        if p_cards_total == d_cards_total:
            print("Its a DRAW")
        elif p_cards_total > d_cards_total:
            print(f"Your Total is {p_cards_total} , dealer cards are {d_cards} and total is {d_cards_total} \nYou WIN")
        else:
            print(f"Your Total is {p_cards_total} , dealer cards are {d_cards} and total is {d_cards_total} \n")
            print("You LOSE")


# check if dealer needs card
def dealer_needs_card(dealer_cards):
    dealer_total = calc_total(dealer_cards, 'dealer')

    if dealer_total < 17:
        new_card = random.choice(cards)
        dealer_cards.append(new_card)
    else:
        print(f"Dealer cards exceeds 17 so no new card needed to add.")
        return


print("---WELCOME TO BLACKJACK GAME----")

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# random .sample selects more than one random number
player_cards = random.sample(cards, 2)
dealer_cards = random.sample(cards, 2)

# show Player Cards
print(f"Your Card = {player_cards}")

# show Dealer Cards - Only one Card from the dealer is shown
show_dealer_cards = dealer_cards.copy()
show_dealer_cards[1] = 'X'
print(f"Dealer Card = {show_dealer_cards}")


def hit_again():
    player_bust = check_bust(player_cards,'player')

    if player_bust:
        print("You loose")
        print(f"Your card is {player_cards} and your total exceeds 21")
    else:
        h_or_s = input("Hit or Stay? ")

        if h_or_s == 'hit':
            hit(player_cards)
            hit_again()
        elif h_or_s == 'stay':
            # stay - check if dealer card is less than 17
            dealer_needs_card(dealer_cards)
            get_result(player_cards, dealer_cards)


hit_again()
