from player_2 import Player

class Lizard:
    def __init__(self) -> None:
        pass

    def lizard_comparison(self, player1, player2):
        if(player2.gesture == 'paper' or player2.gesture == 'spock'):
            player1.score +=1
            print("Player 1 wins round")
        else:
            player2.score +=1
            print("Player 2 wins round.")