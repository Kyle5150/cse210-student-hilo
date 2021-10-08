from game.player import Player

class Dealer:

    def __init__(self):

        self.keep_playing = True
        self.score = 300
        self.player = Player()
    
    def start_game(self):

        while self.keep_playing:

            print(f"The card is: {}")
            user_guess = input("Higher or lower? [h/l] ")
            print(f"The next card was: {}")

    def compare(self):
        pass
