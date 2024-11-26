import random 

for _ in range(10):
    print("\n")
    
random_number = random.randint(1,10)
print('Random Number',random_number)
guesses = []
game_over = 0
guess = -1

def checkGuess(guesss):
    global game_over
    current_guess = int(guesss)
    if current_guess != random_number:
        print('wrong')
    elif current_guess == random_number:
        print('Correct you win!')
        game_over = 1


while game_over != 1:
    if len(guesses) == 0:
        guess = input("I'm thinking of a number between 1 and 100. You have five guesses. Begin by typing your first guess.")
        checkGuess(guess)
    else:
        guess = input("Guess again.")
        checkGuess(guess)
    guesses.append(guess)
