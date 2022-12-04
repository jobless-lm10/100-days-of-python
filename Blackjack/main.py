# from replit import clear
from art import logo
import random

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}


def deal_card():
    return random.choice(list(cards.keys()))


def reduce_aces(cards_list):
    for i in range(len(cards_list)):
        if cards_list[i] == 11:
            cards_list[i] = 1
            break
    return cards_list


def compare(player_cards, dealer_cards):
    if sum(player_cards) == 21:
        return "You got Blackjack. You win 😊"
    elif sum(dealer_cards) == 21:
        return "Dealer got Blackjack. You lose 😢"
    elif sum(dealer_cards) == sum(player_cards):
        return "Match. You Draw 😔"
    elif sum(dealer_cards) > sum(player_cards):
        return "Dealer wins. You lose 😢"
    else:
        return "You win 😊"


def play_blackjack():
    # clear()
    print(logo)
    player_cards = []
    dealer_cards = []
    player_current_score = []
    dealer_current_score = []
    result = ""

    for i in range(2):
        player_cards.append(deal_card())
        player_current_score.append(cards[player_cards[i]])
        dealer_cards.append(deal_card())
        dealer_current_score.append(cards[dealer_cards[i]])
    print(f"Your cards: {player_cards}, current score: {sum(player_current_score)}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    pass_flag = False
    while not pass_flag and sum(player_current_score) != 21:
        if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            drawn_card = deal_card()
            player_cards.append(drawn_card)
            player_current_score.append(cards[drawn_card])
            if sum(player_current_score) > 21:
                player_current_score = reduce_aces(player_current_score)
                if sum(player_current_score) > 21:
                    pass_flag = True
                    result = "You went over. You lose 😢"
            print(f"Your cards: {player_cards}, current score: {sum(player_current_score)}")
        else:
            pass_flag = True

    print(f"Dealer cards: {dealer_cards}, current score: {sum(dealer_current_score)}")
    while sum(dealer_current_score) < 17:
        drawn_card = deal_card()
        dealer_cards.append(drawn_card)
        dealer_current_score.append(cards[drawn_card])
        if sum(dealer_current_score) > 21:
            dealer_current_score = reduce_aces(dealer_current_score)
            if sum(dealer_current_score) > 21:
                result = "Dealer went over. You win 😊"
        print(f"Dealer cards: {dealer_cards}, current score: {sum(dealer_current_score)}")

    print(f"Your final hand: {player_cards}, final score: {sum(player_current_score)}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {sum(dealer_current_score)}")

    if result == "":
        result = compare(player_current_score, dealer_current_score)
    print(result)

    if input("Do you want to continue playing. Type 'y' or 'n': ") == "y":
        play_blackjack()


if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_blackjack()
