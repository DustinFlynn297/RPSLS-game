from player import Player
import random

class AI(Player):
    def __init__(self) -> None:
        super().__init__()
        self.gesture = self.select_gesture()

    def select_gesture(self):
        ai_selection = random.choice(self.gesture)