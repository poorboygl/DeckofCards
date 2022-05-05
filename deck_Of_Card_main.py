
import time
import turtle as tt
from ProviderRepository import providerRepository

provider = providerRepository()
wn = tt.Screen()
wn.bgcolor('black')
wn.setup(800,600)
wn.title('Deck of Cards Similator By NQV')
pen = tt.Turtle()
pen.hideturtle()
pen.speed(0)

# card = provider.card('A','S')
# card.print_card()
# card.render(0,0,pen)

#create deck
deck = provider.deck()
deck.reset_deck()
star_x = -250
for x in range(5):
    card = provider.card('','')
    card.render(star_x+x*125,0,pen)
time.sleep(3)
#render 10 cards in a row
star_x = -250
for x in range(5):
    card = deck.get_Card()
    card.render(star_x+x*125,0,pen)


wn.mainloop()