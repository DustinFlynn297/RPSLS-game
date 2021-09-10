class Game:
    def __init__(self) -> None:
        self.rules = ''
        


    def run_game(self):
        self.welcome()

    
    def welcome(self):
        print(f'Welcome to our game: Rock, Paper, Scissors, Lizard, Spock. \n Here are the rules: \n Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, and Scissors decapitates Lizard. The game is best 2 out of 3')

