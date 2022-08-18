import random

play_game = 'y'

while (play_game== 'y'):
    answer = random.randint(1, 100)
    try_number = input('Guess a number between 1 and 100: ')
    try_number = int(try_number)
    counter = 1

    while try_number != answer:
        if try_number > answer:
            print('Your number is too high.')
        if try_number < answer:
            print('Your number is too low.')
        try_number = int(input('Guess a number between 1 and 100: '))
        counter = counter + 1
    print('Correct. You tried ' + str(counter) + ' times.')
    play_game = input('Continue? ')
