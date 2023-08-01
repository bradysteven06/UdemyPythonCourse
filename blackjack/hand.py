class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1

    def show_first_card(self):
        print(self.cards[0])

    def show_all_cards(self):
        for card in self.cards:
            print(card)

