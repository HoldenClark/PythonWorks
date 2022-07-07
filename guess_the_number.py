#import a random integer and store it.

from random import randint

active = True

#while loop to loop the inputs of the user until they guess the correct number

while active:
    number = randint(1, 10)
    number = int(number)

    prompt = "\nGuess the random number (1-10):"
    prompt += "\n(Enter 'quit' to quit.) "

    guess = input(prompt)

    if guess == 'quit':
        break
    else:
        guess = int(guess)
        if number == guess:
            print("You guessed the correct number!")
        else:
            print("Wrong number!")