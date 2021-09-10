class Game:
    def __init__(self) -> None:
        self.rules = ''


    def run_game(self):
        self.welcome()

    def rules(self):
        pass

    def welcome(self):
        print(f'Welcome to our game: Rock, Paper, Scissors, Lizard, Spock. \n Here are the rules {self.rules}')