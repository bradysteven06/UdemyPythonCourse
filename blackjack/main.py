from player import Player
from deck import Deck


if __name__ == '__main__':
    print("Blackjack")

    # Create a deck of 52 cards
    # Shuffle the deck
    # Ask the Player for their bet
    # Make sure that the Player's bet does not exceed their available chips
    # Deal two cards to the Dealer and two cards to the Player
    # Show only one of the Dealer's cards, the other remains hidden
    # Show both of the Player's cards
    # Ask the Player if they wish to Hit, and take another card
    # If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again
    # If a Player Stands, play the Dealer's hand.
    #   The dealer will always Hit until the Dealer's value meets or exceeds 17
    # Determine the winner and adjust the Player's chips accordingly
    # Ask the Player if they'd like to play again

    new_deck = Deck()
    kevin = Player("Kevin")
    dealer = Player("Dealer")
    game_over = False

    new_deck.shuffle()
    kevin.add_cards(new_deck.deal_one())
    kevin.add_cards(new_deck.deal_one())
    kevin.show_first_card()
    kevin.show_all_cards()


    #while not game_over:
    #    current_bet = 0

