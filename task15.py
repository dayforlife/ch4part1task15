import random


class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print(f"{self.suit} of {self.value}")

class Deck():
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ["Spades", "Clubs", "Diamond", "Hearts"]:
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(s, v))
                

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        
    def drawCard(self):
        return self.cards.pop()
        print(self.cards)


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

# deck = Deck()
# deck.shuffle()
# deck.show()
# deck.build()
# deck.show()
# deck.drawCard()
# player = Player("Adi")
# player.draw(deck).draw(deck)
# player.showHand()
# player.discard()