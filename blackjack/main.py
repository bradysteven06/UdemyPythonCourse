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


def ask_to_hit():
    while True:
        response = input("Would you like to hit?(y/n) ")
        if response == 'y' or response == 'n':
            return response
        else:
            print("Invalid input. Please enter y for yes or n for no.")


def calculate_winner():
    if player.hand.value > 21:
        print(f"{player.name} busts. {dealer.name} wins")
        player.chips.lost_bet()
    elif dealer.hand.value > 21:
        print(f"{dealer.name} busts. {player.name} wins")
        player.chips.won_bet()
    elif dealer.hand.value < player.hand.value:
        print(f"{player.name} win's")
        player.chips.won_bet()
    elif player.hand.value < dealer.hand.value:
        print(f"{dealer.name} win's")
        player.chips.lost_bet()
    else:
        print("It's a draw")


def ask_keep_playing():
    while True:
        response = input("Would you like to keep playing?(y/n) ")
        if response == 'y' or response == 'n':
            return response
        else:
            print("Invalid input. Please enter y for yes or n for no.")


if __name__ == '__main__':

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

    playing = True
    dealer = Player("Dealer")

    print("Let's Blackjack")
    player = Player(input("What's your name? "))
    while playing:
        new_deck = Deck()
        new_deck.shuffle()
        player.place_bet(ask_for_bet(player.chips.total))

        for num in range(2):
            player.hand.add_cards(new_deck.deal_one())
            dealer.hand.add_cards(new_deck.deal_one())

        print(player)
        dealer.hand.show_first_card()

        asking_to_hit = True
        while asking_to_hit and player.hand.value < 22:
            if ask_to_hit() == 'y':
                player.hit(new_deck)
                print(player)
            else:
                asking_to_hit = False

        while dealer.hand.value < 17 and player.hand.value < 22:
            dealer.hit(new_deck)

        print(player)
        print(dealer)
        calculate_winner()
        if player.chips.total == 0 or ask_keep_playing() == 'n':
            playing = False

    print(f"{player.name} has {player.chips.total} chips remaining")
