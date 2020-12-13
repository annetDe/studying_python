import random


def blackjack_rule():
    print(
        '''
        You will get 2 cards. Then you can get as many cards as you wish.
        If sum of your cards is equal 21 - you WIN your bet 1:1
        If sum of your cards is more than 21 - you LOSE your bet
        You can RETURN your bet while sum of your cards is less than 21
        ---
        The value of cards two through ten is their pip value (2 through 10).
        Face cards (Jack, Queen, and King) are all worth ten.
        Aces can be worth one or eleven:
            11 while the total amount is not more than 21, then 1
        '''
    )


def blackjack_game(player):
    game_continue = 'y'
    while game_continue == 'y':
        while True:
            try:
                bet = int(input('Place your bet: '))
            except ValueError:
                continue
            if bet <= player.points:
                break
            else:
                print("You don't have enough points")

        card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(card_deck)
        player_cards = []
        player_cards.append(card_deck.pop())
        player_cards.append(card_deck.pop())

        while True:
            player_pts = player_points(player_cards)
            if player_pts == 21:
                print('You win!')
                print(f'Your cards: {player_cards}')
                player.b_games_won += 1
                player.points += bet
                break
            elif player_pts > 21:
                print('You lose.')
                print(f'Your cards: {player_cards}')
                player.b_games_lose += 1
                player.points -= bet
                break
            else:
                print(
                    f'Your cards: {player_cards}'
                    f'\nYour current points: {player_pts}'
                )
                another_card = input('Take another card? (y/n) ')
                if another_card == 'y':
                    player_cards.append(card_deck.pop())
                else:
                    print('Bet return.')
                    player.b_games_return += 1
                    break
        game_continue = input('\nContinue Blackjack? (y/n) ')


def player_points(list):
    if sum(list) > 21:
        for i in range(len(list)):
            if list[i] == 11:
                list[i] = 1
    return sum(list)
