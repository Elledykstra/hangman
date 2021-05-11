
# HangmanApp
# by Cindy Tra, Miles Groussman, Elle Dykstra
# May 2021
import random
from words import word_list

 #def get_words():
     #word = random.choice(word_list)
     #return word.upper()
 
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters =[]
    guesed_words = []
    tries=6
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("PLease guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice guess,", guess, "is in the word!")
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
            print(display_hangman(tries))
            print(word_completion)
            print("\n")
    if guessed:
        print("Congrats, you guessed the word! you won!")
    else:
        print("Sorry, you ran out of tries, the word was " + word +". Maybe next time")
            
        
    
x=400
y=400


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
    display()
    
# Man

def display():
    # Pole
    stroke(200)
    strokeWeight(5)
    line(x+80, y+130, x+80, y-160)
    line(x+130, y+130, x+30, y+130)
    line(x+80, y-160, x-20, y-160)
    line(x-20, y-160, x-20, y-120)
    
def main():
    word = get_word()
    play(word)
    while input("Play Again?").upper == () == "Y":
        word = get_word()
        play(word)
#print("\n")
#if_name_== "_main_":
    main()
