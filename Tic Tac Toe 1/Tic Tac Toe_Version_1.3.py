# Tic-Tac-Toe Game Version (1.3) The Gameplay Update!  What's New ? :
# Fixing Bugs ( playing with a friend was corrupted )
# Better Code Managment and readibility, adding the notion of gameplays, and dealing with each one seperatly

import random

print("Welcome To Tic Tac Toe !\nGame Version: 1.3\n")


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


# Function for mode selection
def choose_mode():
    mode = input("Choose a mode:\n1. Play with a friend\n2. Play with the computer\n")
    while mode not in ['1', '2']:
        mode = input("Invalid input. Please choose 1 or 2.\n")
    return mode


# Function for choosing player symbols
def players_symbol():
    player_symbol = input("Do You Want to play as X or O: ")
    while player_symbol not in ['X', 'O']:
        player_symbol = input("Invalid input. Please choose X or O.\n")

    if player_symbol == "X":
        return "X", "O"
    else:
        return "O", "X"


# Gameplay function for mode 1
def gameplay_mode_1(board, players, current_player):
    print(f"Player {players[current_player]}'s turn")
    move = input("Enter your move (1-9): ")
    while True:
        if move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            move = input("Invalid move. Please choose a valid move (1-9): ")
        elif board[int(move)] != ' ':
            move = input("Invalid move. Please choose an empty cell: ")
        else:
            board[int(move)] = players[current_player]
            break


# Gameplay function for mode 2
def gameplay_mode_2(board, player_symbol, computer_symbol, current_player):
    if current_player == 1:
        print("Your turn")
        move = input("Enter your move (1-9): ")
        while True:
            if move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                move = input("Invalid move. Please choose a valid move (1-9): ")
            elif board[int(move)] != ' ':
                move = input("Invalid move. Please choose an empty cell: ")
            else:
                board[int(move)] = player_symbol
                break
    else:
        print("Computer's turn")
        move = str(random.randint(1, 9))
        while board[int(move)] != ' ':
            move = str(random.randint(1, 9))
        board[int(move)] = computer_symbol


# Function to play the Game
def play_game():
    board = [' '] * 10
    players = [' ', 'X', 'O']
    current_player = 1
    computer_symbol = ""
    player_symbol = ""

    mode = choose_mode()

    if mode == '2':
        player_symbol, computer_symbol = players_symbol()

        # Ensure the player who selects 'O' plays second
        current_player = 2 if player_symbol == "O" else 1

    while True:
        print_board(board)

        if mode == '1':
            gameplay_mode_1(board, players, current_player)
        else:
            gameplay_mode_2(board, player_symbol, computer_symbol, current_player)

        if check_win(board):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if ' ' not in board[1:]:
            print_board(board)
            print("It's a draw!")
            break

        current_player = 3 - current_player


# Starting the game
play_game()
