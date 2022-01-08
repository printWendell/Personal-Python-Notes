import random


def run_guess(guess, answer):
    if 0 < guess < 11: 
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False

answer = random.randint(1, 10)

# only run this if this is the main file being run
if __name__ == '__main__': 
    while True: 
        try: 
            guess = int(input('guess a number 1~10: '))
            if run_guess(guess, answer): 
                break
        except ValueError:
            print('please enter a number')
            continue

