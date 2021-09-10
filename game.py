class Game:
    def __init__(self) -> None:
        self.style = ''
        


    def run_game(self):
        self.welcome()
        self.playstyle()
    
    def welcome(self):
        print(f'Welcome to our game: Rock, Paper, Scissors, Lizard, Spock. \n Here are the rules: \n Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, and Scissors decapitates Lizard. The game is best 2 out of 3')

    def playstyle(self):
        self.style = input('Would you like to play single player or multiplayer?')
        if (self.style == 'single player'):
            player1 = Human()
            player2 = AI()
        else:
            player1 = Human()
            player2 = Human()

    def player_selection(self):
        pass

    def display_selection(self):
        pass

    def compare_gestures(self):
        pass
        # if (f"{player.selection} == 'rock' && {ai.selection} == 'scissors'"):
        #     player.score += 1
        # elif (play)