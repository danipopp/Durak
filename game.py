# import libraries
import random

# Constant Cards
VALUES = ['2','3','4','5','6','7','8','9','10','B','D','K','A']
SUITS = ['Clubs','Hearts','Spades','Diamonds']

class Cards:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class DeckOfCards:
    def __init__(self):
        self.cards = [Cards(suit,value) for suit in SUITS for value in VALUES]
        random.shuffle(self.cards)

    def pop_cards(self):
        return self.cards.pop() if self.cards else None

class Player:
     
    pass

class Game:
    # TODO
    pass


