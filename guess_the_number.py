import random

guessText = 'Take a guess.'
genNum = random.randint(1, 20)
guessNum = 0
guessed = 0

print('I\'m thinking of a number between 1 and 20.')
print(guessText)
print(str(genNum))

# 5 guesses available
while guessed < 5:
    try:
        guessNum = int(input())
        guessed = guessed + 1
    except:
        print('You did not enter a number.')
        continue

    if guessed < 5:
        if guessNum < genNum:
            print('Your guess is too low.')
            print(guessText)
        elif guessNum > genNum:
            print('Your guess is too high.')
            print(guessText)
        elif guessNum == genNum:
            break
    
    
if guessed >= 5:
    print('The random number is ' + str(genNum) + '!')
else:
    print('Good job! You did it in ' + str(guessed) + ' guesses!')