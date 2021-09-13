from player import Player
import random

class AI(Player):
    def __init__(self) -> None:
        super().__init__()
        self.ai_name()

    def select_gesture(self):       
        self.gesture = random.choice(self.list_of_gestures)

    def ai_name(self):
        name = ["rob", "bob", "steve", "kevin"]
        self.name = random.choice(name)