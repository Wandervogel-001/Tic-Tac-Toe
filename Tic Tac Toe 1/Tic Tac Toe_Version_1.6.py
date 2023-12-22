# Tic-Tac-Toe Game Version (1.6): The AI Update! What's new ? :
# Adding diffuculity [easy], [Hard]
# Adding AI to the computer's moves [ added depth, and fixed bugs ]

import random

print("Welcome To Tic Tac Toe !\nGame Version: 1.6\n")


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


# Function for choosing Difficulty
def choose_difficulty():
    difficulty = input("Choose a Difficulty:\n1.[Easy]\n2.[Hard]\n")
    while difficulty not in ['1', '2']:
        difficulty = input("Invalid input. Please choose 1 or 2.\n")
    return difficulty


# Function for choosing player symbols
def players_symbol():
    player_symbol = input("Do You Want to play as X or O: ")
    while player_symbol.upper() not in ['X', 'O']:
        player_symbol = input("Invalid input. Please choose X or O: ")

    if player_symbol.upper() == "X":
        return "X", "O"
    else:
        return "O", "X"


# Function to search for empty_indices
def empty_indices(board):
    return [i for i, spot in enumerate(board) if spot == ' ' and i != 0]


# Function for evaluating the board        
def evaluate(board, depth, current_player):
    if check_win(board):
        if current_player == 1:
            return depth - 10
        else:
            return 10 - depth
    elif ' ' not in board[1:]:
        return 0


# Function for Minimax Algorithm
def minimax(board, depth, maximizingPlayer, player_symbol, computer_symbol, current_player):
    if check_win(board) or ' ' not in board[1:]:
        return evaluate(board, depth, current_player)
    depth += 1

    if maximizingPlayer:
        max_eval = float('-inf')
        for move in empty_indices(board):
            board[move] = computer_symbol
            evaluation = minimax(board, depth, False, player_symbol, computer_symbol, 3 - current_player)
            board[move] = ' '
            max_eval = max(max_eval, evaluation)
        return max_eval
    else:
        min_eval = float('inf')
        for move in empty_indices(board):
            board[move] = player_symbol
            evaluation = minimax(board, depth, True, player_symbol, computer_symbol, 3 - current_player)
            board[move] = ' '
            min_eval = min(min_eval, evaluation)
        return min_eval


# Function to get the computer's move in Hard Diffuclty
def minimax_move(board, player_symbol, computer_symbol, current_player):
    # Implement the minimax algorithm using the provided logic
    if current_player == 2:  # Computer's turn
        best_move = 0
        best_score = float('-inf')

        for move in empty_indices(board):
            board[move] = computer_symbol
            score = minimax(board, 1, False, player_symbol, computer_symbol, current_player)  
            board[move] = ' '

            if score > best_score:
                best_score = score
                best_move = move

        return best_move


# Function to get the computer's move in Easy Diffuclty
def get_easy_computer_move(board):
    move = str(random.randint(1, 9))
    while board[int(move)] != ' ':
        move = str(random.randint(1, 9))
    return int(move)


# Function for getting the computer's move
def get_computer_move(board, player_symbol, computer_symbol, difficulty, current_player):
    if difficulty == '1':
        return get_easy_computer_move(board)
    elif difficulty == '2':
        if len(empty_indices(board)) == 9:
            # If the board is empty, make a random move
            return get_easy_computer_move(board)
        else:
            return minimax_move(board, player_symbol, computer_symbol, current_player)


# Function for getting the players move
def get_player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Invalid move. Please choose a valid move (1-9)")
        elif board[int(move)] != ' ':
            print("Invalid move. Please choose an empty cell")
        else:
            return int(move)


# Gameplay function for mode 1
def gamemode_1(board, players, current_player):
    print(f"Player {players[current_player]}'s Turn")
    move = get_player_move(board)
    board[move] = players[current_player]


# Gameplay function for mode 2
def gamemode_2(board, player_symbol, computer_symbol, current_player, difficulty):
    print("Your Turn" if current_player == 1 else "Computer's Turn")

    if current_player == 1:
        move = get_player_move(board)
    else:
        move = get_computer_move(board, player_symbol, computer_symbol, difficulty, current_player)

    board[move] = player_symbol if current_player == 1 else computer_symbol


# Function to end the game
def game_over(board, players, player_symbol, computer_symbol, current_player, mode):
    if check_win(board):
        print_board(board)  # Display the final board

        if mode == '1':
            print(f'Player {players[current_player]} wins!')
        else:
            if current_player == 1:
                print(f'Player {player_symbol} wins!')
            else:
                print(f'Player {computer_symbol} wins!')

        return True

    if ' ' not in board[1:]:
        print_board(board)  # Display the final board in case of a draw
        print("It's a tie!")
        return True
    return False


# Function to play the Game
def play_game():
    board = [' '] * 10  # for testing the minimax function: [' ', ' ', 'O', 'O', 'X', ' ', 'X', 'O', ' ', 'X']
    players = [' ', 'X', 'O']
    current_player = 1
    computer_symbol = ""
    player_symbol = ""
    difficulty = ""

    mode = choose_mode()

    if mode == '2':
        difficulty = choose_difficulty()
        player_symbol, computer_symbol = players_symbol()

        # Ensure the player who selects 'O' plays second
        current_player = 2 if player_symbol == "O" else 1

    while True:
        print_board(board)
        if mode == '1':
            gamemode_1(board, players, current_player)
        else:
            gamemode_2(board, player_symbol, computer_symbol, current_player, difficulty)

        if game_over(board, players, player_symbol, computer_symbol, current_player, mode):
            break

        current_player = 3 - current_player


# Starting the game
play_game()
