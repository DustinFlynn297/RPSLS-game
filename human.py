from player import Player

class Human(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name_selection()
        

    def name_selection(self):
        self.name = input("What is your name? ")

    def select_gesture(self):
        self.gesture = input("Please select a gesture form this list: \n Rock \n Paper \n Scissors \n Lizard \n Spock \n").lower()
