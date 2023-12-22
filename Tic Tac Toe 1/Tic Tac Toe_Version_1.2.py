# Tic-Tac-Toe Game Version (1.2) X and O Update!  What's New ? :
# Fixing Bug ( chosing between X and O had no impact previsouly )
# Better Invalid inputs Handling ( Handling occupied cells and out of range seperatly )
# The option between X and O has an impact on the game as follows:
# Who Ever choses X, plays first, and choosing a symbol results in playing with it


import random

print("Welcome To Tic Tac Toe !\nGame Version: 1.2\n")


# Function to print the board
def print_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


# Function to check for a win
def check_win(board):
    # Check rows
    for i in range(1, 8, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True
    # Check columns
    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
    # Check diagonals
    if board[1] == board[5] == board[9] != ' ':
        return True
    if board[3] == board[5] == board[7] != ' ':
        return True
    return False


# Function to play the game
def play_game():
    board = [' '] * 10
    players = [' ', 'X', 'O']
    current_player = 1
    computer_symbol = ""
    player_symbol = ""

    # Ask for player mode
    mode = input("Choose a mode:\n1. Play with a friend\n2. Play with the computer\n")
    while mode not in ['1', '2']:
        mode = input("Invalid input. Please choose 1 or 2.\n")

    # Ask for player player_symbol
    if mode == '2':
        player_symbol = input("Do You Want to play as X or O: ")
        while player_symbol not in ['X', 'O']:
            player_symbol = input("Invalid input. Please choose X or O.\n")

        if player_symbol == "X":
            current_player = 1
            computer_symbol = "O"
        else:
            current_player = 2
            computer_symbol = "X"

    while True:
        print_board(board)

        if mode == '1':
            print(f"Player {players[current_player]}'s turn")
        else:
            if current_player == 1:
                print("Your turn")
            else:
                print("Computer's turn")

        if mode == '1' or (mode == '2' and current_player == 1):
            move = input("Enter your move (1-9): ")
            while True:
                if move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    move = input("Invalid move. Please choose a valid move (1-9): ")
                elif board[int(move)] != ' ':
                    move = input("Invalid move. Please choose an empty cell: ")
                else:
                    # Assign player's symbol if playing with the computer
                    if mode == '2' and current_player == 1:
                        board[int(move)] = player_symbol
                    else:
                        board[int(move)] = computer_symbol
                    break

        else:
            move = str(random.randint(1, 9))
            while board[int(move)] != ' ':
                move = str(random.randint(1, 9))
            board[int(move)] = computer_symbol

        if check_win(board):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if ' ' not in board[1:]:
            print_board(board)
            print("It's a draw!")
            break

        current_player = 3 - current_player


play_game()
