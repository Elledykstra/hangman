# HangmanApp
# by Cindy Tra, Miles Groussman, Elle Dykstra
# May 2021

from Head import Head
from Arm1 import Arm1
from Arm2 import Arm2
from Body import Body
from Leg1 import Leg1 
from Leg2 import Leg2
import random

h1 = Head(400, 400)
a1 = Arm1(400, 400)
a2 = Arm2(400, 400)
b1 = Body(400, 400)
l1 = Leg1(400, 400)
l2 = Leg2(400, 400)
guess = ''

words = ['trench', 'manner', 'depart', 'dilute', 'health', 'report', 'flavor', 'rhythm', 'effect', 'needle', 'camera', 'railcar', 'safety', 'thanks', 'option', 'subway', 'resist', 'reward', 'demand', 'divide', 'squash', 'garlic', 'forest', 'appear', 'hiccup', 'immune', 'unrest', 'sector', 'corner', 'symbol', 'height', 'regret', 'ground', 'memory', 'canvas', 'retain', 'weight', 'polite', 'critic', 'crouch', 'outlet', 'morale', 'safari', 'matter', 'arrest', 'mobile', 'linger', 'bucket', 'runner']
def setup():
    size (800, 800)
    
def draw():    
    background(0, 122, 41)
    textAlign(CENTER)
    textSize(40)
    text('HANGMAN!', width/2, height/2-350)
    textSize(15)
    text('How to play: First, guess a random letter. The more incorrect guesses, the closer you are to losing the game.', width/2, height/2-325)
    text('Make sure that the man does not get hung!', width/2, height/2-305)
    pole()
    
    if keyPressed:
        if key == 'a' or key == 'A':
            showText('A')

    else:
        fill(255)
        
def showText(guess):
    fill(0, 122, 41)
    rect(100, 300, 50, 50)
    fill(255)
    text(guess, 125, 330)

def pole():
    stroke(250)
    strokeWeight(5)
    x = 400
    y = 400
    line(x+80, y+130, x+80, y-160)
    line(x+130, y+130, x+30, y+130)
    line(x+80, y-160, x-20, y-160)
    line(x-20, y-160, x-20, y-120)
    
