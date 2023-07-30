from deck import Deck
from player import Player


def out_of_cards_check(player, player_cards):
    if len(player_cards) == 0:
        if player == "One":
            print("Player One out of cards! Game Over")
            print("Player Two Wins!")
        elif player == "Two":
            print("Player Two out of cards! Game Over")
            print("Player One Wins!")
        return True


if __name__ == '__main__':

    # Create players
    player_one = Player("One")
    player_two = Player("Two")

    # Set up new deck
    new_deck = Deck()
    new_deck.shuffle()

    # Split the Deck between players
    for x in range(int(len(new_deck.all_cards)/2)):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    # Game loop
    game_over = False
    round_count = 0
    while not game_over:

        round_count += 1
        print(f"Round {round_count}")

        # Check to see if a player is out of cards:
        game_over = out_of_cards_check(player_one.name, player_one.all_cards) or out_of_cards_check(player_two.name,
                                                                                                    player_two.all_cards)

        # Game is still on
        if not game_over:

            # Start a new round and reset current cards "on the table"
            player_one_cards = [player_one.remove_one()]
            player_two_cards = [player_two.remove_one()]

            at_war = player_one_cards[-1].value == player_two_cards[-1].value

            while at_war and not game_over:

                print('WAR!')

                # This occurs when the cards are equal.
                # We'll grab another card each and continue the current war.

                # Check to see if a player is out of cards:
                if len(player_one.all_cards) < 5:
                    print("Player One unable to play war! Game Over at War")
                    print("Player Two Wins! Player One Loses!")
                    game_over = True

                elif len(player_two.all_cards) < 5:
                    print("Player Two unable to play war! Game Over at War")
                    print("Player One Wins! Player Two Loses!")
                    game_over = True

                # Otherwise, we're still at war, so we'll add the next cards
                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

                # Check for war condition again
                at_war = player_one_cards[-1].value == player_two_cards[-1].value

            if not game_over:
                if player_one_cards[-1].value > player_two_cards[-1].value:
                    # Player One gets the cards
                    player_one.add_cards(player_one_cards)
                    player_one.add_cards(player_two_cards)

                elif player_one_cards[-1].value < player_two_cards[-1].value:
                    # Player Two gets the cards
                    player_two.add_cards(player_one_cards)
                    player_two.add_cards(player_two_cards)

