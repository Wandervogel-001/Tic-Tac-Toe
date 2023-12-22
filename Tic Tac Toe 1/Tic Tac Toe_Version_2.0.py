# Tic-Tac-Toe Game Version (2.0): The Game Simulator Update! What's new ? :
# added Gamemode 3: responsible for Simulating Games of computer vs computer

import random
import time

print("Welcome To Tic Tac Toe!\nGame Version: 2.0\nCreated By @Youssef_Bouzidi\n")


# Function to print the board
def print_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


# Function to check for the winner
def check_winner(board):
    # Check rows
    for i in range(1, 8, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return board[i]
    # Check columns
    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return board[i]
    # Check diagonals
    if board[1] == board[5] == board[9] != ' ':
        return board[1]
    if board[3] == board[5] == board[7] != ' ':
        return board[3]
    return None


# Function for mode selection
def choose_mode():
    mode = input("Choose a mode:\n1. Play with a friend\n2. Play with the computer\n3. Simulate a Game\n")
    while mode not in ['1', '2', '3']:
        mode = input("Invalid input. Please choose a valid option.\n")
    return mode


# Function for choosing Difficulty
def choose_difficulty(symbol, mode):
    if mode == '2':
        difficulty = input("Choose a Difficulty:\n1.[No Difficulty]\n2.[Easy]\n3.[Normal]\n4.[Hard]\n")
    else:
        difficulty = input(f"Choose The Difficulty for Computer {symbol}:\n1.[No Difficulty]\n2.[Easy]\n3.[Normal]\n4.[Hard]\n")

    while difficulty not in ['1', '2', '3', '4']:
        difficulty = input("Invalid input. Please choose a valid option.\n")
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
def evaluate(board, depth, current_computer, opponent):
    winner = check_winner(board)

    if winner == current_computer:
        return 10 - depth
    elif winner == opponent:
        return depth - 10
    elif ' ' not in board[1:]:
        return 0


# Function for Minimax Algorithm
def minimax(board, depth, maximizingPlayer, current_computer, opponent):
    if check_winner(board) or ' ' not in board[1:]:
        return evaluate(board, depth, current_computer, opponent)
    depth += 1

    if maximizingPlayer:
        max_eval = float('-inf')
        for move in empty_indices(board):
            board[move] = current_computer
            evaluation = minimax(board, depth, False, current_computer, opponent)
            board[move] = ' '
            max_eval = max(max_eval, evaluation)
        return max_eval
    else:
        min_eval = float('inf')
        for move in empty_indices(board):
            board[move] = opponent
            evaluation = minimax(board, depth, True, current_computer, opponent)
            board[move] = ' '
            min_eval = min(min_eval, evaluation)
        return min_eval


# Function to get the computer's move in No Diffuclty
def get_random_computer_move(board):
    move = random.randint(1, 9)
    while board[move] != ' ':
        move = random.randint(1, 9)
    return move


# Function for getting the computer's move in Easy Diffuclty
def get_easy_computer_move(board, player_symbol, players, current_player, mode):
    # Check if there's a winning move
    for move in empty_indices(board):
        board[move] = player_symbol if mode == '2' else players[3 - current_player]
        if check_winner(board):
            board[move] = ' '
            return move
        board[move] = ' '
    # If not, play randomly
    return get_random_computer_move(board)


# Function for getting the computer's move in Normal Difficulty
def get_normal_computer_move(board, player_symbol, computer_symbol):
    # Check if there's a winning or a defensive move
    for symbol in [computer_symbol, player_symbol, 'X', 'O']:
        for move in empty_indices(board):
            board[move] = symbol
            if check_winner(board):
                board[move] = ' '
                return move
            board[move] = ' '
    # If not, play randomly
    return get_random_computer_move(board)


# Function to get the computer's move in Hard Diffuclty
def get_hard_computer_move(board, mode, player_symbol, computer_symbol, players, current_player):
    # If the board is empty, make a random move
    if len(empty_indices(board)) == 9:
        return get_random_computer_move(board)
    else:
        # Determine current computer and opponent
        current_computer = players[current_player] if mode == '3' else computer_symbol
        opponent = players[3 - current_player] if mode == '3' else player_symbol

        # Implement the minimax algorithm using the provided logic
        best_move = 0
        best_score = float('-inf')

        for move in empty_indices(board):
            board[move] = computer_symbol
            score = minimax(board, 1, False, current_computer, opponent)
            board[move] = ' '

            if score > best_score:
                best_score = score
                best_move = move

        return best_move


# Function for getting the computer's move
def get_computer_move(board, player_symbol, computer_symbol, difficulty, players, current_player, mode, computerX_diff, computerO_diff):
    diff = ''
    if mode == '2':
        diff = difficulty
    elif mode == '3':
        diff = computerX_diff if current_player == 1 else computerO_diff

    if diff == '1':
        return get_random_computer_move(board)
    elif diff == '2':
        return get_easy_computer_move(board, player_symbol, players, current_player, mode)
    elif diff == '3':
        return get_normal_computer_move(board, player_symbol, computer_symbol)
    elif diff == '4':
        return get_hard_computer_move(board, mode, player_symbol, computer_symbol, players, current_player)


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
    print_board(board)


# Gameplay function for mode 2
def gamemode_2(board, player_symbol, computer_symbol, current_player, difficulty, mode, players, computerX_diff, computerO_diff):
    print("Your Turn" if current_player == 1 else "Computer's Turn")

    if current_player == 1:
        move = get_player_move(board)
    else:
        move = get_computer_move(board, player_symbol, computer_symbol, difficulty, players, current_player, mode, computerX_diff, computerO_diff)
        time.sleep(.4)

    board[move] = player_symbol if current_player == 1 else computer_symbol
    print_board(board)


# Gameplay function for mode 3
def gamemode_3(board, player_symbol, computer_symbol, current_player, difficulty, mode, players, computerX_diff, computerO_diff):
    print(f"Computer {players[current_player]}'s Turn")

    move = get_computer_move(board, player_symbol, computer_symbol, difficulty, players, current_player, mode, computerX_diff, computerO_diff)
    time.sleep(.85)

    board[move] = players[current_player]
    print_board(board)


# Function to end the game
def game_over(board, players, player_symbol, computer_symbol, current_player, mode, wins, player):
    if check_winner(board):
        if mode == '1':
            print(f'Player {players[current_player]} wins!')
            wins[player] += 1
        elif mode == '2':
            print(f'Player {player_symbol} wins!' if current_player == 1 else f'Player {computer_symbol} wins!')
            wins[player] += 1
        elif mode == '3':
            print(f'Computer {players[current_player]} wins!')
            wins[player] += 1
        return True

    if ' ' not in board[1:]:
        print("It's a tie!")
        wins[' '] += 1
        return True
    return False


# Function for playing the game
def gameplay(board, players, player_symbol, computer_symbol, current_player, mode, total_wins, difficulty, computerX_diff, computerO_diff):
    wins = {'X': 0, 'O': 0, ' ': 0}  # Wins for the current game
    player = ''

    while True:
        if mode == '1':
            gamemode_1(board, players, current_player)
            player = players[current_player]
        elif mode == '2':
            gamemode_2(board, player_symbol, computer_symbol, current_player, difficulty, mode, players, computerX_diff, computerO_diff)
            player = player_symbol if current_player == 1 else computer_symbol
        elif mode == '3':
            gamemode_3(board, player_symbol, computer_symbol, current_player, difficulty, mode, players, computerX_diff, computerO_diff)
            player = players[current_player]

        if game_over(board, players, player_symbol, computer_symbol, current_player, mode, wins, player):
            break

        current_player = 3 - current_player

    # Update total wins
    total_wins['X'] += wins['X']
    total_wins['O'] += wins['O']
    total_wins[' '] += wins[' ']


# Function for displaying Wins, loses and Draws
def display_wins_loses_draws(mode, player_symbol, total_wins):
    if mode == '1':
        print("\nTotal Wins:")
        print("Player X: [ {} ]\nPlayer O: [ {} ]\nDraws:    [ {} ]".format(total_wins['X'], total_wins['O'], total_wins[' ']))
    elif mode == '2':
        if player_symbol == 'X':
            print("\nWins:  [ {} ]\nLoses: [ {} ]\nDraws: [ {} ]".format(total_wins['X'], total_wins['O'], total_wins[' ']))
        else:
            print("\nWins:  [ {} ]\nLoses: [ {} ]\nDraws: [ {} ]".format(total_wins['O'], total_wins['X'], total_wins[' ']))
    else:
        print("\nTotal Wins:")
        print("Computer X: [ {} ]\nComputer O: [ {} ]\nDraws:      [ {} ]".format(total_wins['X'], total_wins['O'], total_wins[' ']))


# Function for starting the game
def start_the_game():
    while True:
        board = [' '] * 10
        board_display = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        players = [' ', 'X', 'O']
        current_player = 1
        computer_symbol = ""
        player_symbol = ""
        computerx_diff = ''
        computero_diff = ''
        difficulty = ""
        total_wins = {'X': 0, 'O': 0, ' ': 0}

        mode = choose_mode()

        if mode == '2':
            difficulty = choose_difficulty('', '2')
            player_symbol, computer_symbol = players_symbol()

            # Ensure the player who selects 'O' plays second
            current_player = 2 if player_symbol == "O" else 1
        elif mode == '3':
            computerx_diff = choose_difficulty('X', '3')
            computero_diff = choose_difficulty('O', '3')

        print("Board: ")
        print_board(board_display)

        # Play The Game
        gameplay(board, players, player_symbol, computer_symbol, current_player, mode, total_wins, difficulty, computerx_diff, computero_diff)
        display_wins_loses_draws(mode, player_symbol, total_wins)

        while True:
            menu_choice = input("\nChoose an option:\n1.[Retry]\n2.[Restart]\n3.[Quit]\n")
            while menu_choice not in ['1', '2', '3']:
                menu_choice = input("Please choose a valid option: ")
            if menu_choice == '1':
                board = [' '] * 10  # Reset the board
                print("Board: ")
                print_board(board_display)
                gameplay(board, players, player_symbol, computer_symbol, current_player, mode, total_wins, difficulty, computerx_diff, computero_diff)
                display_wins_loses_draws(mode, player_symbol, total_wins)
            elif menu_choice == '2':
                break
            elif menu_choice == '3':
                print("Thanks for playing! :3")
                time.sleep(1)
                return


# Starting the game
start_the_game()
