from hand import Hand
from chips import Chips


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.chips = Chips()

    def __str__(self):
        return f"{self.name}'s Hand: {', '.join(map(str, self.hand.cards))} (Value: {self.hand.value})"

    def hit(self, deck):
        self.hand.add_cards(deck.deal_one())
        self.adjust_for_ace()

    def adjust_for_ace(self):
        # checks for aces in the hand and adjusts the value
        while self.hand.value > 21 and self.hand.aces:
            self.hand.value -= 10
            self.hand.aces -= 1

    def place_bet(self, bet_amount):
        self.chips.bet = bet_amount

    def win_bet(self):
        self.chips.won_bet()

    def lose_bet(self):
        self.chips.lost_bet()

    def clear_hand(self):
        self.hand.cards = []
        self.hand.value = 0
        self.hand.aces = 0
