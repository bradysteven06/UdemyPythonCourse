from deck import Deck
from player import Player

if __name__ == '__main__':

    my_deck = Deck()
    print(len(my_deck.all_cards))
    print(my_deck.all_cards[0])
    my_deck.shuffle()
    print(my_deck.all_cards[0])
    my_card = my_deck.deal_one()
    print(my_card)
    print(len(my_deck.all_cards))
    steven = Player("Steven")
    print(steven)
    steven.add_cards(my_card)
    print(steven)
    print(steven.all_cards[0])
