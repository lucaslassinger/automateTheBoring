from random import randint
lowerBound = input('Enter a lower bound:')
upperBound = input('Enter an Upper bound:')

lowerBound=int(lowerBound)
upperBound=int(upperBound)

while True:
    if upperBound > lowerBound:
        break
    else:
        upperBound = input('Please enter an upper bound greater then ' +str(lowerBound) +':')
        upperBound = int(upperBound)

number = randint(lowerBound,upperBound)

print('I am thinking of a number between ' + str(lowerBound) + ' and ' + str(upperBound)+ '. Guess my number:')

guess = input()
guess = int(guess)

while True:
    if guess == number:
        print('You win!')
        break
    elif guess <= number:
        guess = input('Your guess was too low, please enter a new guess:')
        guess = int(guess)

    elif guess >= number:
        guess = input('Your guess was too high, please enter a new guess:')
        guess = int(guess)


