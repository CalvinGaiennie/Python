import random 
random_number = random.randint(1,10)
print(random_number)
guesses = []
game_over = 0
guess = input("I'm thinking of a number between 1 and 100. You have five guesses. Begin by typing your first guess.")

while game_over != 1:
    if guess != random_number:
        print('wrong')
        guess = input('Guess again')

if guess == random_number:
    print('Correct')
    game_over = 1