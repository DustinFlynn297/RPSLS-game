from player import Player
import random

class AI(Player):
    def __init__(self) -> None:
        super().__init__()
        self.select_gesture()
        self.ai_name()

    def select_gesture(self):
        gesture = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.gesture = random.choice(gesture)

    def ai_name(self):
        name = ["rob", "bob", "steve", "kevin"]
        self.name = random.choice(name)