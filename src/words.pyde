import random
words = ['trench', 'manner', 'depart', 'dilute', 'health', 'report', 'flavor', 'rhythm', 'effect', 'needle', 'camera', 'railcar', 'safety', 'thanks', 'option', 'subway', 'resist', 'reward', 'demand', 'divide', 'squash', 'garlic', 'forest', 'appear', 'hiccup', 'immune', 'unrest', 'sector', 'corner', 'symbol', 'height', 'regret', 'ground', 'memory', 'canvas', 'retain', 'weight', 'polite', 'critic', 'crouch', 'outlet', 'morale', 'safari', 'matter', 'arrest', 'mobile', 'linger', 'bucket', 'runner']
words = random.choice(words)
turns = 6
while turns > 0:
    failed = 0
for char in word:
    if char in guesses:
        print(char)
    else:
        print("_")
        failed += 1
        
if failed == 0:
    print('You Win')
    print('the word is :', word)

guess = input('guess another letter:')
guesses += guess
if guess not in word:
    turns -= 1
    print ('Wrong')
    print("you have", + turns, 'more guesses')
    
    if turns == 0: 
        print('You Lose')
