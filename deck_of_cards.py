from enum import Enum

# Requirements: Make sure you ask about the scope of the project, make no assumsions.
# How many cards in the deck? 52
# How man suits? 4
# Which suits? clubs diamonds hearts spades
# Is there a particular format you'd like the deck of cards in?

class Suit(Enum):
    clubs = 0
    diamonds = 1
    hearts = 2
    spades = 3


class Card():
    def __init__(self, suit, card_num):
        # check if suit is actually in Suit Enum
        self.suit = suit
        self.card_num = card_num
    def __repr__(self):
        return "{} of {}".format(self.card_num, self.suit)
    def __str__(self):
        return "{} of {}".format(self.card_num, self.suit)

def build_deck(size) -> Card:
    card_num = 1
    deck = []
    for i in range(size):
        deck.append(Card(Suit(i%4), card_num))
        if deck[i].suit == Suit.spades:
            card_num = card_num+1
    
    return deck

print("Enter size of deck:")
deck_size = input()

deck = build_deck(int(deck_size))

print(deck)

print("Enter index of deck:")
deck_i = input()

print(deck[int(deck_i)])