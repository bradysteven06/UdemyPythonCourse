from player import Player
from deck import Deck


def ask_for_bet(total_chips):
    while True:
        bet = input(f"You have {total_chips} chips. How many do you bet? ")
        try:
            bet = int(bet)
            if 0 < bet <= total_chips:
                return bet
            else:
                print(f"Invalid bet. You must bet at least 1 chip and no more than {total_chips} chips.")
        except ValueError:
            print("Invalid input. Please enter a number.")


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
    playing = True
    player = Player("Kevin")
    dealer = Player("Dealer")
    bob = Player("Bob")

    new_deck.shuffle()
    player.place_bet(ask_for_bet(player.chips.total))

    for num in range(2):
        player.hand.add_cards(new_deck.deal_one())
        dealer.hand.add_cards(new_deck.deal_one())

    print(player.chips.bet)
    print(player)
    print(dealer)
