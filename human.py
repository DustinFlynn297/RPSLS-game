from player import Player

class Human(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name_selection()
        

    def name_selection(self):
        self.name = input("What is your name? ")
        self.name_validation()

    def select_gesture(self):
        self.gesture = input("Please select a gesture from this list: " + " " + self.list_of_gestures[0] + ", " + self.list_of_gestures[1] + ", " + self.list_of_gestures[2] + ", " + self.list_of_gestures[3] + ", " + self.list_of_gestures[4] + "\n").lower()
        self.gesture_validation()

    def gesture_validation(self):
        if (self.gesture == 'rock' or self.gesture == 'paper' or self.gesture == 'scissors' or self.gesture == 'lizard' or self.gesture == 'spock'):
            pass
        else:
            print("Invalid gesture selection, please try again")
            self.select_gesture()

    def name_validation(self):
        if (len(self.name) == 0):
            self.name_selection()
        else:
            pass
