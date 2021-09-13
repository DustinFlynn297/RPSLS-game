from human import Human
from ai import AI

class Game:
    def __init__(self) -> None:
        self.style = ''
        self.player1 = ''
        self.player2 = ''        
        self.run_game()
        


    def run_game(self):
        self.welcome()
        self.playstyle()
        self.
        self.display_selection()
        
    
    def welcome(self):
        print(f'Welcome to our game: Rock, Paper, Scissors, Lizard, Spock. \n Here are the rules: \n Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, and Scissors decapitates Lizard. The game is best 2 out of 3')

    def playstyle(self):
        self.style = input('Would you like to play single player or multiplayer?').lower()
        if (self.style == 'single player'):
            self.player1 = Human()
            self.player2 = AI()
        else:
            self.player1 = Human()
            self.player2 = Human()

    def display_selection(self):
        print(f"{self.player1.name} has chosen {self.player1.gesture} and {self.player2.name} has chosen {self.player2.gesture}")



    def compare_gestures(self):
        self.player1.select_gesture()
        self.player2.select_gesture()
        self.display_selection()
        if (self.player1.gesture == self.player2.gesture):
            print("You two have tied, please select another gesture.")            
            self.player1.select_gesture()
            self.player2.select_gesture()
            self.display_selection()
            
        elif (self.player1.gesture == 'rock'):
            if (self.player2.gesture == 'scissors'or 'lizard'):
                self.player1.score += 1
                print("Player 1 wins round")
            else:
                self.player2.score +=1
                print("Player 2 wins round.")
        elif(self.player1.gesture == 'scissors'):
            if(self.player2.gesture == 'paper' or 'lizard'):
                self.player1.score += 1
                print("Player 1 wins round")
            else:
                self.player2.score +=1
                print("Player 2 wins round.")
        elif(self.player1.gesture == 'paper'):
            if(self.player2.gesture == 'rock' or 'spock'):
                self.player1.score += 1
                print("Player 1 wins round")
            else:
                self.player2.score +=1
                print("Player 2 wins round.")
        elif(self.player1.gesture == 'lizard'):
            if(self.player2.gesture == 'paper' or 'spock'):
                self.player1.score +=1
                print("Player 1 wins round")
            else:
                self.player2.score +=1
                print("Player 2 wins round.")
        elif(self.player1.gesture == 'spock'):
            if(self.player2.gesture == 'rock' or 'scissors'):
                self.player1.score +=1
                print("Player 1 wins round")
            else:
                self.player2.score +=1
                print("Player 2 wins round.")

            
            




        #     player.score += 1
        # elif (play)

