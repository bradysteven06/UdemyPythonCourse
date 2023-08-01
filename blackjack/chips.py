
class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def won_bet(self):
        self.total += self.bet

    def lost_bet(self):
        self.total -= self.bet
