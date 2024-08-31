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
    def __init__(self,name):
         self.name = name
         self.hand= []
    
    def draw(self,deck):
        self.hand.append(deck.pop_cards())

    def __repr__(self):
        return f"{self.name}: {', '.join(map(str, self.hand))}"
    

class Game:
    def __init__(self):
        self.deck = DeckOfCards()
        self.players = [Player("Ksyusha"), Player("Daniel")]
        self.trump = self.deck.cards[-1].suit
        self.dealCards()
        self.currentAttackerIndex = 0
        self.currentDefenderIndex = 1
        

    def dealCards(self):
        for i in range(6):
            for player in self.players:
                player.draw(self.deck)

    def playGame(self):
        attacker = self.players[self.currentAttackerIndex]
        defender = self.players[self.currentDefenderIndex]

        attackCard = attacker.pop(0)
        print(f"{attacker.name} attacks with {attackCard}")

        defenderCard = None
        for card in defender.hand:
            if attackCard.suit != self.trump:
                if VALUES.index(card.value) > VALUES.index(attackCard.value):
                    defenderCard = card
                    break
                elif card.suit == self.trump:
                    defenderCard = card
                    break
            else:
                if VALUES.index(card.value) > VALUES.index(attackCard.value):
                    defenderCard = card
                    break

        if defenderCard:
            # TODO
            pass

