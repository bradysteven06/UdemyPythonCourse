class Player:

    def __init__(self, name):
        self.name = name
        self.chips = 0
        # A new player has no cards
        self.all_cards = []

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

    def show_first_card(self):
        print(self.all_cards[0])

    def show_all_cards(self):
        for card in self.all_cards:
            print(card)
