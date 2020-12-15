import json

from player import Player
from magic import magic_rule, magic_game
from blackjack import blackjack_rule, blackjack_game


def main():
    name = input('Enter your name: ')

    try:
        with open('stat.json') as f:
            players_data = json.load(f)
    except FileNotFoundError:
        players_data = []

    player = isexisted_player(players_data, name)

    casino_continue = 'y'
    while casino_continue == 'y':
        choice = 0
        while choice not in (1, 2, 3, 4, 5):
            try:
                choice = main_menu()
            except ValueError:
                continue

        if choice == 1:
            magic_rule()
            magic_game(player)

        elif choice == 2:
            blackjack_rule()
            blackjack_game(player)

        elif choice == 3:
            player.print_stat()

        elif choice == 4:
            for d in players_data:
                if d['name'] == name:
                    players_data.remove(d)
                    break
            del player
            name = input('Enter your name: ')
            player = isexisted_player(players_data, name)

        elif choice == 5:
            existed_player = 0
            new_players_data = players_data
            for d in new_players_data:
                if d['name'] == name:
                    d.update(player.__dict__)
                    existed_player = 1
                    break
            if existed_player == 0:
                new_players_data.append(player.__dict__)

            with open('stat.json', 'w') as f:
                data = json.dumps(new_players_data, indent=4)
                f.write(data)

            casino_continue = 'n'


def main_menu():
    choice = int(input(
        '\nMain menu:'
        '\n1 Magic'
        '\n2 Blackjack (21)'
        '\n3 View statistics'
        '\n4 Reset game progress'
        '\n5 Leave the casino\n'
    ))
    return choice


def isexisted_player(players_data, name):
    tmp = next((i for i in players_data if i['name'] == name), {})
    if tmp:
        player = Player(
                        tmp['name'],
                        tmp['points'],
                        tmp['m_games_won'],
                        tmp['m_games_lose'],
                        tmp['record_counter'],
                        tmp['b_games_won'],
                        tmp['b_games_lose'],
                        tmp['b_games_return']
        )
    else:
        player = Player(name)
    return player


main()
