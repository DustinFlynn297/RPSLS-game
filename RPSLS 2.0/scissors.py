class Scissors:
    def __init__(self, player1, player2) -> None:
        self.scissors_comparison(player1, player2)

    def scissors_comparison(self, player1, player2):
        if(player2.gesture == 'paper' or player2.gesture == 'lizard'):
            player1.score += 1
            print("Player 1 wins round")
        else:
            player2.score +=1
            print("Player 2 wins round.")