from player_2 import Player
import random

class AI(Player):
    def __init__(self) -> None:
        super().__init__()
        self.ai_name()

    def select_gesture(self):       
        self.gesture = random.choice(self.list_of_gestures).lower()

    def ai_name(self):
        name = ["Rob", "Bob", "Steve", "Kevin"]
        self.name = random.choice(name)