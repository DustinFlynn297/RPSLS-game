class Spock:
    def __init__(self, player1, player2) -> None:
        self.spock_comparison(player1, player2)

    def spock_comparison(self, player1, player2):
        if(player2.gesture == 'rock' or player2.gesture == 'scissors'):
            player1.score +=1
            print("Player 1 wins round")
        else:
            player2.score +=1
            print("Player 2 wins round.")
