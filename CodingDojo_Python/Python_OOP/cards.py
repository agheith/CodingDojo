import random
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck(object):
    def __init__(self):
        self.deck = []
        self.suits = ["spades", "diamonds","hearts", "clubs"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for i in self.values:
            for j in self.suits:
                self.deck.append(Card(j,i))

    def randomCard(suite, value):
        pass

    def deal(self):
        random.randrange(0,5)
        print self.deck[random.randrange(0,52)].value
        print self.deck[random.randrange(0,52)].suite

deck = Deck()
deck.deal()
