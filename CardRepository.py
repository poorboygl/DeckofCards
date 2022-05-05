
import turtle as tt
class Card():
    def __init__(self,name = None,suit = None):
        self.name = name
        self.suit = suit
        #diamonds (♦), clubs (♣), hearts (♥) and spades (♠)  
        self.symbols = {'D':'♦','C':'♣','H':'♥','S':'♠'} #dictionary

    def print_card(self):
        if self.suit == 'S':
            symbol ='♠'
        print(f'{self.name}{self.symbols[self.suit]}')
    
    def render(self,x,y,pen : tt.Turtle):
        #draw border
        pen.penup()
        pen.goto(x,y)
        pen.color('blue')
        pen.goto(x-50, y+75)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x+50,y+75)
        pen.goto(x+50,y-75)
        pen.goto(x-50,y-75)
        pen.goto(x-50,y+75)
        pen.end_fill()
        pen.penup()

        if self.name !='':
        #Draw suit in the middle
            pen.color('white')
            pen.goto(x-18,y-30)
            pen.write(self.symbols[self.suit], False,font=('Courier New', 48,'normal'))

            #Draw top left
            pen.goto(x-40, y+45)
            pen.write(self.name, False,font=('Courier New', 18,'normal'))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False,font=('Courier New', 18,'normal'))

            #Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False,font=('Courier New', 18,'normal'))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False,font=('Courier New', 18,'normal'))




