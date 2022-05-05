from CardRepository import Card
import random
class Deck():
    def __init__(self):
        self.cards = []
        names = ('A','K','Q','J','10','9','8','7','6','5','4','3','2')
        suits = ('D','C','H','S')

        for name in names:
            for suit in suits:
                card = Card(name,suit)
                self.cards.append(card)
    
    def Shuffle(self):
        random.shuffle(self.cards)
    
    def get_Card(self):
        card = self.cards.pop()
        return card
    
    def reset_deck(self):
        self.cards = []
        names = ('A','K','Q','J','10','9','8','7','6','5','4','3','2')
        suits = ('D','C','H','S')

        for name in names:
            for suit in suits:
                card = Card(name,suit)
                self.cards.append(card)
        self.Shuffle()

#Test
#deck = Deck() #một đối tượng đầy đủ do có ()
#card = Card  #một tham chiếu

