import random

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# As the game progresses, possible moves are decreasing, while used_moves are expanded
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


def start_game():
    for row in board:
        for value in row:
            print(f'[{value}]', end=' ')
        print()


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
        if user_choice.lower() == 'exit':
            return user_choice
        try:
            chosen_number = int(user_choice)
        except ValueError:
            print('No number given. Please try again. You can also type "exit" to quit. ')
            continue
        if chosen_number in possible_moves and chosen_number not in used_moves:
            possible_moves.remove(int(user_choice))
            used_moves.append(chosen_number)
            hor_i = number_to_position_map[chosen_number][0]
            ver_i = number_to_position_map[chosen_number][1]
            return hor_i, ver_i, user_choice
        elif chosen_number in used_moves:
            print('This field has already been marked!')
            break

        else:
            print('The input is invalid')
            break


def update_board(horizontal_i, vertical_i, computer=False):
    new_board = board
    if computer:
        new_board[horizontal_i][vertical_i] = 'o'
    else:
        new_board[horizontal_i][vertical_i] = 'x'
    return new_board


def check_if_winning(board, sign):
    for row in board:
        if row == [sign, sign, sign]:
            return True
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False


def computer_marks():
    if possible_moves:
        computer_move = random.choice(possible_moves)
        possible_moves.remove(computer_move)
        used_moves.append(computer_move)
        hor_i = number_to_position_map[computer_move][0]
        ver_i = number_to_position_map[computer_move][1]
        return hor_i, ver_i,
    else:
        return None


def main():
    global board
    start_game()
    while True:
        print(possible_moves)
        if check_if_winning(board, 'x'):
            print(f'Player X won!')
            return
        elif check_if_winning(board, 'o'):
            print('Player O won!')
        elif not possible_moves:
            print('It is a draw!')
            return
        move = ask_for_input()
        if move == 'exit':
            print('Quitting...')
            return
        print(f'Player X put an x on field {move[2]}.')
        board = update_board(move[0], move[1])
        print_board(board)
        if check_if_winning(board, 'x'):
            print('Player X won!')
            return

        if check_if_winning(board, 'o'):
            print('Player O won!')
            return

        computer_move = computer_marks()
        if computer_move:
            print('Now it\'s the opponent\'s turn!')
            board = update_board(
                computer_move[0], computer_move[1], computer=True)
            print_board(board)

        if check_if_winning(board, 'o'):
            print('Player 0 won!')
            return

        elif not possible_moves:
            print('It is a draw!')
            return


if __name__ == '__main__':
    main()
