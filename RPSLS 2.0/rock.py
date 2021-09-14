class Rock:
    def __init__(self, player1, player2) -> None:
        self.rock_comparison(player1, player2)

    def rock_comparison(self, player1, player2):
        if (player2.gesture == 'scissors' or player2.gesture == 'lizard'):
            player1.score += 1
            print("Player 1 wins round")
        else:
            player2.score +=1
            print("Player 2 wins round.")