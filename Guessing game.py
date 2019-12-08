from random import randint
# to generate a number between 1 & 9
number = randint(1,9)
# to find the number of guesses after the game is done
guesses = []
# just to initiate the variable
guess = 0
# loop to maintain the user untill correct guess is provided
while number != guess:
    guess = int(input('Guess a number, or type "exit" to end the game\n'))
    # to give the user an option to end the game if he doesn't want to play
    if guess == 'exit':
        break
    guesses.append(guess)
    # to let the user to go high, low or if he won
    if guess > number:
        print('your guess is too high !!')
    elif guess < number:
        print('your guess is too low !!')
    else:
        print('You guessed it CORRECTLY in {} times !!'.format(len(guesses)))
