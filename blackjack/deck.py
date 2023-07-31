import random
from card import Card


class Deck:
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank, Deck.values[rank]))

    def shuffle(self):
        # Shuffles the list all_cards
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Remove one card from the list of all_cards
        return self.all_cards.pop()