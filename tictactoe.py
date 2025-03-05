import random

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

board_art = {'empty': ("┌─────────┐",
                       "│         │",
                       "│         │",
                       "│         │",
                       "└─────────┘"),
             'x': ("┌─────────┐",
                   "│   \ /   │",
                   "│    X    │",
                   "│   / \   │",
                   "└─────────┘"),
             'o': ("┌─────────┐",
                   "│    ︵   │",
                   "│  (   )  │",
                   "│    ︶   │",
                   "└─────────┘")}


def print_board(board):
    for row in board:
        for value in board:
            if value.lower() == 'x':
                print(board_art['x'], end=' ')
            elif value.lower() == 'o':
                print(board_art['o'], end=' ')
            else:
                print(board_art['empty'], end=' ')
        print()


def ask_for_input():
    while True:
        user_choice = input('Choose field you would like to mark: ')
        if int(user_choice) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            number_to_position_map = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                                      4: (1, 0), 5: (1, 1), 6: (1, 2),
                                      7: (2, 0), 8: (2, 1), 9: (2, 2)}
            hor_i = number_to_position_map[user_choice][0]
            ver_i = number_to_position_map[user_choice][1]

            return hor_i, ver_i

        else:
            print('The input is invalid')
            break


def update_board(horizontal_i, vertical_i):
    new_board = board
    new_board[horizontal_i][vertical_i] = 'X'
    return new_board


def check_if_winning(board):
    winning = False
    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
        winning = True
    elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        winning = True
    elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        winning = True
    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
        winning = True
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        winning = True
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
        winning = True
    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        winning = True
    elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
        winning = True


print(board)
x = update_board(1, 1)
print(x)
