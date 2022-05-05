from CardRepository import Card
from DeskRepository import Deck

class providerRepository :
    def __init__(self) :
        self._card = None
        self._deck = None
    
    @property
    def card(self):
        if self._card == None:
            self._card = Card
        return self._card

    @property
    def deck(self):
        if self._deck == None:
            self._deck = Deck
        return self._deck


