# HangmanApp
# by Cindy Tra, Miles Groussman, Elle Dykstra
# May 2021

from Head import Head
h1 = Head(380,380)

def setup():
    size (800, 800)
    
def draw():
    background(0, 122, 41)
    textAlign(CENTER)
    textSize(40)
    text('HANGMAN!', width/2, height/2-350)
    textSize(15)
    text('How to play: First, guess a random letter. The more incorrect guesses, the closer you are to losing the game.', width/2, height/2-325)
    text("Make sure the man doesn't get hung!", width/2, height/2-305)
    pole() 
    h1.displayHead()
    
x = 380
y = 380
def pole():
    stroke(200)
    strokeWeight(5)
    line(x+80, y+130, x+80, y-160)
    line(x+130, y+130, x+30, y+130)
    line(x+80, y-160, x-20, y-160)
    line(x-20, y-160, x-20, y-120)
