# HangmanApp
# by Cindy Tra, Miles Groussman, Elle Dykstra
# May 2021
import random 
from Words import word_list

def setup():
    size (800, 800)

def draw():    
    background(0, 122, 41)
    textAlign(CENTER)
    textSize(40)
    text('HANGMAN!', width/2, height/2-350)
    textSize(15)
    text('How to play: First, guess a random letter. The more guesses incorrect, the closer you are to losing the game.', width/2, height/2-330)
    text('Make sure that the man doesnt get hung!', width/2, height/2-315)
