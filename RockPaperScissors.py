from tkinter import *
import time
import random

from matplotlib.pyplot import sci
from pyparsing import Or     
def games(self):
    rock=1;
    paper=2;
    scis=3;
    player1=random.randint(1,3)
    player2=random.randint(1,3)
    if (player1==rock&player2==paper)or(player1==paper&player2==scis)or(player1==scis&player2==rock):
        print("PLAYER-2 won")
    if(player1==player2):
        print("DRAW")
    else:
        print("PLAYER-1 won")
            
            
        
     
        
game=Tk()
game.title("ROCK PAPER GAME")
game.geometry('400x400')
Canvas=Canvas(game,width=1000,height=750,bg="Black")
Canvas.create_text(200,50,text="ROCK PAPER SCISORRS",fill="white",font=("Helvetica 15 bold"))
Canvas.pack()
player1_label =Label(Canvas, text = 'PLAYER', font=('calibre',15, 'bold'))
player2_entry=Entry(Canvas, textvariable =player2, font = ('calibre',15,'normal'))
self.games() 
game.mainloop()