import random

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
used_moves = []

# board_art = {'empty': ("┌─────────┐",
#                        "│         │",
#                        "│         │",
#                        "│         │",
#                        "└─────────┘"),
#              'x': ("┌─────────┐",
#                    "│   \ /   │",
#                    "│    X    │",
#                    "│   / \   │",
#                    "└─────────┘"),
#              'o': ("┌─────────┐",
#                    "│    ︵   │",
#                    "│  (   )  │",
#                    "│    ︶   │",
#                    "└─────────┘")}

board_art = {'empty': "[ ]",
             'x': "[X]",
             'o': '[O]'}


def print_board(board):
    for row in board:
        for value in row:
            if str(value).lower() == 'x':
                print(board_art['x'], end=' ')
            elif str(value).lower() == 'o':
                print(board_art['o'], end=' ')
            else:
                print(board_art['empty'], end=' ')
        print()


number_to_position_map = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                          4: (1, 0), 5: (1, 1), 6: (1, 2),
                          7: (2, 0), 8: (2, 1), 9: (2, 2)}


def ask_for_input():
    while True:
        user_choice = input('Choose field you would like to mark: ')
        chosen_number = int(user_choice)
        if chosen_number in possible_moves and chosen_number not in used_moves:
            possible_moves.remove(int(user_choice))
            used_moves.append(chosen_number)
            hor_i = number_to_position_map[chosen_number][0]
            ver_i = number_to_position_map[chosen_number][1]

            return hor_i, ver_i
        elif chosen_number in used_moves:
            print('This field has already been marked!')
            break

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
    return winning


def computer_marks():
    computer_move = random.choice(possible_moves)
    possible_moves.remove(computer_move)
    used_moves.append(computer_move)
    hor_i = number_to_position_map[computer_move][0]
    ver_i = number_to_position_map[computer_move][1]
    return hor_i, ver_i


def main():
    global board
    while possible_moves and check_if_winning(board) is False:
        move = ask_for_input()
        board = update_board(move[0], move[1])
        print_board(board)
        computer_move = ask_for_input()
        board = update_board(computer_move[0], computer_move[1])
        print_board(board)


if __name__ == '__main__':
    main()
