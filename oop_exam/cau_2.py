import random

SUITS = ["♠", "♣", "♥", "♦"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

VALUES = {}
for rank in RANKS:
    if rank in ["J", "Q", "K"]:
        VALUES[rank] = 10
    elif rank == "A":
        VALUES[rank] = 1
    else:
        VALUES[rank] = int(rank)


class Card:
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit

    @property
    def rank(self):
        return self.__rank

    def __str__(self):
        # dunder method (double underscore)
        return f"{self.__rank}{self.__suit}"

    def value(self):
        return VALUES[self.__rank]


class Deck:
    def __init__(self):
        self.__cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.__cards.append(Card(suit, rank))
        random.shuffle(self.__cards)

    def draw(self, num):
        drawn_cards = []
        for _ in range(num):
            drawn_cards.append(self.__cards.pop(0))
        return drawn_cards


def calculate_score(cards):
    total_value = 0
    for card in cards:
        total_value += card.value()
    return total_value % 10


def get_highest_card(cards):
    highest_card = cards[0]
    for card in cards[1:]:
        if SUITS.index(card.suit) > SUITS.index(highest_card.suit):
            highest_card = card
        elif SUITS.index(card.suit) == SUITS.index(highest_card.suit):
            if RANKS.index(card.rank) > RANKS.index(highest_card.rank):
                highest_card = card
    return highest_card


def determine_winner(player1_cards, player2_cards):
    score1 = calculate_score(player1_cards)
    score2 = calculate_score(player2_cards)
    print(
        f"Player 1's cards: {[str(card) for card in player1_cards]} - Score: {score1}"
    )
    print(
        f"Player 2's cards: {[str(card) for card in player2_cards]} - Score: {score2}"
    )

    if score1 > score2:
        print("Player 1 wins!")
    elif score1 < score2:
        print("Player 2 wins!")
    else:
        highest_card1 = get_highest_card(player1_cards)
        highest_card2 = get_highest_card(player2_cards)
        if SUITS.index(highest_card1.suit) > SUITS.index(highest_card2.suit):
            print("Player 1 wins by high card!")
        elif SUITS.index(highest_card1.suit) < SUITS.index(highest_card2.suit):
            print("Player 2 wins by high card!")
        else:
            if RANKS.index(highest_card1.rank) > RANKS.index(highest_card2.rank):
                print("Player 1 wins by high card rank!")
            else:
                print("Player 2 wins by high card rank!")


deck = Deck()
player1_cards = deck.draw(3)
player2_cards = deck.draw(3)

determine_winner(player1_cards, player2_cards)
