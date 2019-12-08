from random import randint 
number = randint(1,9)
print(number)
guesses = []
guess = 0
while number != guess:
    guess = input('Guess a number, or type "exit" to end the game\n')
    if guess == 'exit':
        break
    guess = int(guess)
    guesses.append(guess)
    if guess > number:
        print('your guess is too high !!')
    elif guess < number:
        print('your guess is too low !!')
    else:
        print('You guessed it CORRECTLY in {} times !!'.format(len(guesses)))
