# Tic-Tac-Toe Game Version (1.0)
# Game Version : Simple Tic-Tac-Toe, play against a friend

print("Welcome To Tic Tac Toe !\nGame Version: 1.0")

# Create the game board
board = [' ' for _ in range(9)]


# Function to print the board
def print_board():
    print('--------------')
    for i in range(2, -1, -1):
        print('|', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
        print('--------------')


# Function to check for a win
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False


# Function to play the game
def play_game():
    player = 'X'
    while True:
        print_board()
        position = int(input("Player " + player + ", enter a position (1-9): ")) - 1
        if board[position] == ' ':
            board[position] = player
            if check_win(player):
                print_board()
                print("Player " + player + " wins!")
                break
            if ' ' not in board:
                print_board()
                print("It's a Draw!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")


# Start the game
play_game()
