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

words = ['trench', 'manner', 'depart', 'dilute', 'health', 'report', 'flavor', 'rhythm', 'effect', 'needle', 'camera', 'railcar', 'safety', 'thanks', 'option', 'subway', 'resist', 'reward', 'demand', 'divide', 'squash', 'garlic', 'forest', 'appear', 'hiccup', 'immune', 'unrest', 'sector', 'corner', 'symbol', 'height', 'regret', 'ground', 'memory', 'canvas', 'retain', 'weight', 'polite', 'critic', 'crouch', 'outlet', 'morale', 'safari', 'manner', 'arrest', 'mobile', 'linger', 'bucket', 'runner', 'branch']

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

x = 400
y = 400
def pole():
    stroke(250)
    strokeWeight(5)
    line(x+80, y+130, x+80, y-160)
    line(x+130, y+130, x+30, y+130)
    line(x+80, y-160, x-20, y-160)
    line(x-20, y-160, x-20, y-120)
    
def get_words():
    w = random.choice(words)
    return w.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(tries)
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("PLease guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed this letter", guess + '.')
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job!,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Wrong guess.")
            print(tries)
            print(word_completion)
            print("\n")
    if guessed:
        print("Congrats, you guessed the word! You won!")
    else:
        print("Sorry, you ran out of tries, the word was " + word +". Maybe next time!")
        
def main():
    word = get_words()
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)
    print("\n")
    
if __name__ == "__main__":
    main()
