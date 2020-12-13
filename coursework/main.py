from player import Player
from magic import magic_rule, magic_game
from blackjack import blackjack_rule, blackjack_game


def main():
    name = input('Enter your name: ')
    player = Player(name)

    casino_continue = 'y'
    while casino_continue == 'y':
        choice = 0
        while choice not in (1, 2, 3, 4, 5):
            try:
                choice = int(input(
                    '\nMain menu:'
                    '\n1 Magic'
                    '\n2 Blackjack (21)'
                    '\n3 View statistics'
                    '\n4 Reset game progress'
                    '\n5 Leave the casino\n'
                ))
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
            del player
            name = input('Enter your name: ')
            player = Player(name)
        else:
            casino_continue = 'n'


main()
