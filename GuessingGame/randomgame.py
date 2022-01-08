import sys
from random import randint

firstNumber = int(sys.argv[1])
secondNumber = int(sys.argv[2])

answer = randint((firstNumber), (secondNumber))


while True: 
    try: 
        userGuess = int(input(f"Guess a number between {firstNumber} ~ {secondNumber}: "))
        if userGuess == answer: 
            print('your a genius')
            break
        else: 
            print('Guess again')
    except ValueError: 
        print('please enter a number')
        continue
