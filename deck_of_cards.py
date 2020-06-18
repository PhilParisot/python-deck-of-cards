from enum import Enum

# Requirements: Make sure you ask about the scope of the project, make no assumsions.
# How many cards in the deck? 52
# How man suits? 4
# Which suits? clubs diamonds hearts spades
# Is there a particular format you'd like the deck of cards in?

class Suit(Enum):
    clubs = 1
    diamonds = 2
    hearts = 3
    spades = 4


class Card():
    def __init__(self, suit, card_num):
        # check if suit is actually in Suit Enum
        self.suit = suit
        self.card_num = card_num


class Deck:
    def __init__(self, card, size):
        self.card = card
        self.size = size
        self.deck

    def _build_deck:
        counter = 1
        for i in range(self.size):
            
            if suit == Suit.spades:
                counter = counter+1

    deck = 
    return deck


class Animal:
    def __init__(self, size, sound):
        self.size = size
        self.sound = sound

    def make_noise(self):
        print(self.sound)
        
dog = Animal('medium', 'woof')