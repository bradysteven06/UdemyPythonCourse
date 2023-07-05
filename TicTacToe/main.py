
def display_instructions():
    print(f"Let's play Tic Tac Toe!")
    print(f'Match three in a row to win.')
    print(f'Player 1 is X and Player 2 is O.')
    print(f'Game start!')


def display_board(board):
    print(f'   |   |   ')
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print(f'___|___|___')
    print(f'   |   |   ')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print(f'___|___|___')
    print(f'   |   |   ')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')
    print(f'   |   |   ')


def create_board():
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    return board


def get_move():
    move = input('insert move')
    return move


def make_move():
    valid_move = get_move()


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


if __name__ == '__main__':

    display_instructions()
    game_board = create_board()
    display_board(game_board)
    print(check_win(game_board))



