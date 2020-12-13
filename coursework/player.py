class Player:
    name = None
    points = 10
    m_games_won = 0
    m_games_lose = 0
    record_counter = 999
    b_games_won = 0
    b_games_lose = 0
    b_games_return = 0

    def __init__(self, name):
        self.name = name

    @property
    def m_games_played(self):
        return self.m_games_won + self.m_games_lose

    @property
    def m_win_rate(self):
        if self.m_games_played:
            return round(self.m_games_won / self.m_games_played, 2)
        else:
            return '-'

    @property
    def b_games_played(self):
        return self.b_games_won + self.b_games_lose + self.b_games_return

    @property
    def b_win_rate(self):
        if self.b_games_played:
            return round(self.b_games_won / self.b_games_played, 2)
        else:
            return '-'

    def print_stat(self):
        print(
            f'\nPlayer name: {self.name}'
            f'\nPlayer points: {self.points}'
            '\n\nMagic'
            f'\nTotal games played: {self.m_games_played}'
            f'\nGames won: {self.m_games_won}'
            f'\nWin rate: {self.m_win_rate}'
            f'\nRecord number of attempts: {self.record_counter}'
            '\n\nBlackjack'
            f'\nTotal games played: {self.b_games_played}'
            f'\nGames won: {self.b_games_won}'
            f'\nWin rate: {self.b_win_rate}'
        )
