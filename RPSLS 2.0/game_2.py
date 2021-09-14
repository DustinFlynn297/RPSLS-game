from human_2 import Human
from ai_2 import AI
from paper import Paper
from scissors import Scissors
from rock import Rock
from lizard import Lizard
from spock import Spock

class Game:
    def __init__(self) -> None:
        self.style = ''
        self.player1 = ''
        self.player2 = ''        
        self.run_game()
        


    def run_game(self):
        self.welcome()
        self.playstyle()
        self.compare_gestures()
        self.end_game()       
    
    
    def welcome(self):
        print(f'Welcome to our game: Rock, Paper, Scissors, Lizard, Spock. \n Here are the rules: \n Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, and Scissors decapitates Lizard. The game is best 2 out of 3')

    def playstyle(self):
        self.style = input('Would you like to play single player or multiplayer? ').lower()
        if (self.style == 'single player'):
            self.player1 = Human()
            self.player2 = AI()
        elif (self.style == 'multiplayer'):
            self.player1 = Human()
            self.player2 = Human()
        else:
            print("Invalid input, please input a valid option")
            self.playstyle()

    def display_selection(self):
        print(f"{self.player1.name} has chosen {self.player1.gesture} and {self.player2.name} has chosen {self.player2.gesture}")



    def compare_gestures(self):
        rock = Rock()
        paper = Paper()
        scissors = Scissors()
        lizard = Lizard()
        spock = Spock()
        while (self.player1.score < 2 and self.player2.score < 2):
            self.player1.select_gesture()
            self.player2.select_gesture()
            self.display_selection()
            if (self.player1.gesture == self.player2.gesture):
                print("You two have tied, please select another gesture.")            
                self.compare_gestures()            
            elif (self.player1.gesture == 'rock'):
                rock.rock_comparison(self.player1, self.player2)
            elif(self.player1.gesture == 'scissors'):
                scissors.scissors_comparison(self.player1, self.player2)                
            elif(self.player1.gesture == 'paper'):
                paper.paper_comparison(self.player1, self.player2)                
            elif(self.player1.gesture == 'lizard'):
                lizard.lizard_comparison(self.player1, self.player2)
            elif(self.player1.gesture == 'spock'):
                spock.spock_comparison(self.player1, self.player2)
            
            
    def end_game(self):
        if(self.player1.score > self.player2.score):
            print(f"{self.player1.name} has won the match!")
        else:
            print(f"{self.player2.name} has won the match!")