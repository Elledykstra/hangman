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
    alphabet()

def pole():
    stroke(250)
    strokeWeight(5)
    x = 400
    y = 400
    line(x+80, y+130, x+80, y-160)
    line(x+130, y+130, x+30, y+130)
    line(x+80, y-160, x-20, y-160)
    line(x-20, y-160, x-20, y-120)
    
def showText(guess):
    fill(0, 122, 41)
    rect(100, 300, 50, 50)
    fill(255)
    text(guess, 125, 330)
    
def alphabet():
    if keyPressed:
        if key == 'a' or key == 'A':
            showText('A')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'b' or key == 'B':
            showText('B')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'c' or key == 'C':
            showText('C')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'd' or key == 'D':
            showText('D')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'e' or key == 'E':
            showText('E')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'f' or key == 'F':
            showText('F')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'g' or key == 'G':
            showText('G')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'h' or key == 'H':
            showText('h')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'i' or key == 'I':
            showText('I')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'j' or key == 'J':
            showText('J')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'k' or key == 'K':
            showText('K')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'l' or key == 'L':
            showText('L')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'm' or key == 'M':
            showText('M')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'n' or key == 'N':
            showText('N')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'o' or key == 'O':
            showText('O')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'p' or key == 'P':
            showText('P')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'q' or key == 'Q':
            showText('Q')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'r' or key == 'R':
            showText('R')
    else:
        fill(255)
        
    if keyPressed:
        if key == 's' or key == 'S':
            showText('S')
    else:
        fill(255)
        
    if keyPressed:
        if key == 't' or key == 'T':
            showText('T')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'u' or key == 'U':
            showText('U')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'v' or key == 'V':
            showText('V')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'w' or key == 'W':
            showText('W')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'x' or key == 'X':
            showText('X')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'y' or key == 'Y':
            showText('Y')
    else:
        fill(255)
        
    if keyPressed:
        if key == 'z' or key == 'Z':
            showText('Z')
    else:
        fill(255)
