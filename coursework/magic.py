import random


def magic_rule():
    print(
        '''
        Try to guess the magic number from 1 to 100.
        I will give you hints: more or less.
        You have 10 attempts to guess the number.
        1 attempt = 10 pts
        2 attempts = 9 pts
        3 attempts = 8 pts
        4 attempts = 7 pts
        5 attempts = 6 pts
        6 attempts = 5 pts
        7 attempts = 4 pts
        8 attempts = 3 pts
        9 attempts = 2 pts
        10 attempts = 1 pts
        lose = -10 pts
        '''
    )


def magic_game(player):
    game_continue = 'y'
    while game_continue == 'y':
        random_number = random.randint(1, 100)  # случайное число от a до b
        user_number = counter = 0
        while user_number != random_number:
            try:
                user_number = int(input('Magic number is: '))
                counter += 1
            except ValueError:
                continue

            if user_number == random_number:
                player.m_games_won += 1
                player.points += 11 - counter
                print('\nCongratulations! Magic number is ', user_number)
                if counter < player.record_counter:
                    print('NEW record! Attempts: ', counter)
                    player.record_counter = counter
                else:
                    print('Attempts: ', counter)
            elif counter == 10:
                player.m_games_lose += 1
                player.points -= 10
                counter = 0
                print('Game over. Wrong attempts are 10.')
                break
            elif user_number < random_number:
                print('No, magic number MORE than', user_number)
            else:
                print('No, magic number LESS than', user_number)

        game_continue = input('\nContinue Magic? (y/n) ')
