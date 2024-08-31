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
        self.cards = [Cards(value,suit) for suit in SUITS for value in VALUES]
        random.shuffle(self.cards)

    def pop_cards(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self,name):
         self.name = name
         self.hand= []
    
    def draw(self,deck):
        self.hand.append(deck.pop_cards())

    def playCard(self, card):
        defense = self.hand.pop(card)
        return defense 

    def __repr__(self):
        return f"{self.name}: {', '.join(map(str, self.hand))}"
    

class Game:
    def __init__(self, ai_vs_ai = False):
        self.deck = DeckOfCards()
        self.players = [Player("Ksyusha"), Player("Daniel")]
        self.trump = self.deck.cards[-1].suit
        self.dealCards()
        self.currentAttackerIndex = 0
        self.currentDefenderIndex = 1
        self.ai_vs_ai = ai_vs_ai
        

    def dealCards(self):
        for i in range(6):
            for player in self.players:
                player.draw(self.deck)

    def playLogic(self):
        attacker = self.players[self.currentAttackerIndex]
        defender = self.players[self.currentDefenderIndex]

        action = -1
        if self.ai_vs_ai:
            pass
        else:
            action = int(input(f"{attacker.name} choose a card to play (0-{len(attacker.hand)-1}) or -1 for playing no Card: "))

        if action >= 0:
            attackCard = attacker.playCard(action)
            print(f"{attacker.name} attacks with {attackCard}")

        defenderCard = None

        if self.ai_vs_ai:
            pass
        else:
            print(f"{defender.name} {defender.hand}")
            defenderCardIndex = int(input(f"{defender.name} choose a card to defend (0-{len(defender.hand)-1}) or -1 for getting all the cards: "))
        
        if defenderCardIndex >= 0:
            card = defender.hand[defenderCardIndex]
            if attackCard.suit != self.trump:
                if VALUES.index(card.value) > VALUES.index(attackCard.value):
                    defenderCard = card
                elif card.suit == self.trump:
                    defenderCard = card
            else:
                if VALUES.index(card.value) > VALUES.index(attackCard.value):
                    defenderCard = card

        if defenderCard:
            defender.playCard(defenderCardIndex)
            print(f"{defender.name} defends with {defenderCard}")
        else:
            defender.hand.append(attackCard)
            print(f"{defender.name} can't defend. {defender.name} picks up the card(s). ")

        # switch roles
        self.currentAttackerIndex, self.currentDefenderIndex = self.currentDefenderIndex, self.currentAttackerIndex

        self.drawCards()

        # Check for game over
        if len(self.deck.cards) == 0 and any(len(player.hand) == 0 for player in self.players):
            print("Game over!")
            return True  # Indicate game over
        
        self.printCards()
        return False
    
    def drawCards(self):
        for player in self.players:
            while len(player.hand) < 6 and self.deck.cards:
                player.draw(self.deck)

    def printCards(self):
        for player in self.players:
            print(player)

    def playGame(self):
        gameOver = False
        while not gameOver:
            gameOver = self.playLogic()

game = Game()

game.playGame()

