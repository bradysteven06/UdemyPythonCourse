
def display_instructions():
    print(f"Let's play Tic Tac Toe!")
    print(f"Match three in a row to win.")
    print(f"Player 1 is X and Player 2 is O.")
    print(f"Game start!")


def display_board(board):
    print(f"   |   |   ")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print(f"___|___|___")
    print(f"   |   |   ")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print(f"___|___|___")
    print(f"   |   |   ")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print(f"   |   |   ")


def create_board():
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    return board


def get_move():
    is_valid = False
    player_move = ""
    while not is_valid:
        player_move = input("Enter your move (1-9): ")

        if not player_move.isdigit():
            print("Invalid input. Please enter a digit.")
        else:
            is_valid = True
    return player_move


def make_move(board, player):
    is_valid = False
    while not is_valid:
        move = get_move()
        if move == '1' and board[0][0] == '1':
            board[0][0] = player
            is_valid = True
        elif move == '2' and board[0][1] == '2':
            board[0][1] = player
            is_valid = True
        elif move == '3' and board[0][2] == '3':
            board[0][2] = player
            is_valid = True
        elif move == '4' and board[1][0] == '4':
            board[1][0] = player
            is_valid = True
        elif move == '5' and board[1][1] == '5':
            board[1][1] = player
            is_valid = True
        elif move == '6' and board[1][2] == '6':
            board[1][2] = player
            is_valid = True
        elif move == '7' and board[2][0] == '7':
            board[2][0] = player
            is_valid = True
        elif move == '8' and board[2][1] == '8':
            board[2][1] = player
            is_valid = True
        elif move == '9' and board[2][2] == '9':
            board[2][2] = player
            is_valid = True
    return board


def check_win(board):
    is_winner = False

    # horizontal check
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        is_winner = True
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        is_winner = True
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        is_winner = True
    # vertical check
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        is_winner = True
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        is_winner = True
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        is_winner = True
    # diagonal check
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        is_winner = True
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        is_winner = True

    return is_winner


def check_play_again():
    is_valid = False
    play_again = False
    while not is_valid:
        choice = input(f"Would you like to play another game? (y/n): ")
        if choice == 'y':
            play_again = True
            is_valid = True
        elif choice == 'n':
            play_again = False
            is_valid = True
        else:
            print(f"Please enter y or n.")
    return play_again


if __name__ == '__main__':

    player1 = "X"
    player2 = "O"
    current_player = player1
    player1_score = 0
    player2_score = 0
    another_game = True

    while another_game:
        game_over = False
        display_instructions()
        game_board = create_board()
        display_board(game_board)
        while not game_over:

            game_board = make_move(game_board, current_player)
            display_board(game_board)
            if check_win(game_board):
                if current_player == player1:
                    print(f"Player 1 wins!")
                    player1_score += 1
                else:
                    print(f"Player 2 wins!")
                    player2_score += 1
                game_over = True
            if current_player == player1 and not game_over:
                current_player = player2
            elif current_player == player2 and not game_over:
                current_player = player1
        if check_play_again():
            another_game = True
        else:
            another_game = False
    print(f"The final score was Player 1: {player1_score} and Player 2: {player2_score}")

