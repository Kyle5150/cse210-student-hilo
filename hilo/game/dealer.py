from random import choice
from game.player import Player

class Dealer:

    def __init__(self):

        self.keep_playing = True
        self.score = 300
        self.player = Player()
        self.user_guess = "l"
    
    def start_game(self):
        
        while self.keep_playing:
            self.get_inputs()
            self.compare()

            


    def get_inputs(self):
        self.player.draw()
        print(f"The card is: {self.player.first_card}")
        self.user_guess = input("Higher or lower? [h/l] ")
        print(f"The next card was: {self.player.next_card}")

    def compare(self):
        
        if self.user_guess.lower() == "l" and self.player.first_card > self.player.next_card:
            self.score += self.player.get_points(True)
        elif self.user_guess.lower() == "h" and self.player.first_card < self.player.next_card:
            self.score += self.player.get_points(True)
        elif self.player.first_card == self.player.next_card:
            print("They were the same. No points are given")
        else:
            self.score += self.player.get_points(False)

    def do_outputs(self):
        print(f"Your score is: {self.score}")
        if self.player.draw_able():
            choice = input("Keep playing? (y/n) ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False