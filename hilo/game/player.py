from random import randint


class Player:

    def __init__(self):
        self.next_card = 1
        self.first_card = 1
        self.can_draw = True
        self.dealer = Dealer()

        
    def draw(self):
        self.first_card = randint(1,13)
        self.next_card = randint(1,13)

    def draw_able(self, score):
        if score <= 0:
            self.can_draw = False

    def get_points(self, compare):
        if compare == True:
            return 100
        elif compare == False:
            return -75
        