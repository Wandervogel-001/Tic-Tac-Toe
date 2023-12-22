# Tic-Tac-Toe 2!
# Game Version: 1.6
# The Gameplay Update! What's new ?:
# added the option to choose the symbol (X or O), modified the code to handle computers moves separately
# added time delay

import pygame
import random
from sys import exit

# Function for drawing the Game Info Messages
def print_welcome():
    screen.fill('White')
    for i, message in enumerate(messages):
        text_surface = game_font.render(message, False, 'Black')
        text_rect = text_surface.get_rect(topleft=(5, 5 + i * 20))
        screen.blit(text_surface, text_rect)

# Fucntion for drawing The Game menu
def print_menu():
    if menu == 1:
        screen.blit(start_surface_scaled, start_rect)
        screen.blit(quit_surface_scaled, quit_rect)
    elif menu == 2:
        screen.blit(mode_surface, mode_rect)
        screen.blit(pvp_surface, pvp_rect)
        screen.blit(pvc_surface, pvc_rect)
    elif menu == 3:
        screen.blit(difficulty_surf, difficulty_rect)
        screen.blit(no_diff_surf, no_diff_rect)
        screen.blit(easy_surf, easy_rect)
        screen.blit(normal_surf, normal_rect)
        screen.blit(hard_surf, hard_rect)
    elif menu == 4:
        screen.blit(symbols_surf, symbols_rect)
        screen.blit(x_surf, x_rect)
        screen.blit(o_surf, o_rect)
    
# Function for drawing the board
def print_board():
    screen.blit(board_surf, board_rect)
    for i, symbol in enumerate(board):
        if symbol == 'X':
            screen.blit(x_symbol, board_rects[i])
        elif symbol == 'O':
            screen.blit(o_symbol, board_rects[i])

# Function for drawing the outro screen
def print_winner():
    print_board()
    winner = check_winner(board)
    if winner == 'X':
        message = winner_messages[0]
    elif winner == 'O':
        message = winner_messages[1]
    else:
        message = winner_messages[2]
        
    message_surface = game_font.render(message, False, 'Black')
    message_surface_scaled = pygame.transform.scale2x(message_surface)
    message_rect = message_surface_scaled.get_rect(center =(225, 430))
    screen.blit(message_surface_scaled, message_rect)

    instruction_message = game_font.render('Press Space to retry', False, 'Black')
    instruction_message_rect = instruction_message.get_rect(center = (225, 475))
    screen.blit(instruction_message, instruction_message_rect)

# Function for reseting the board
def reset_board():
    global board, current_player, player_symbol, mode
    board = [' '] * 9
    current_player = 1

# Function for reseting the game
def reset_game():
    global board, game_active, current_player, menu_active, player_symbol, mode
    if not menu_active:
        if menu in [3, 5] and not game_active:
            board = [' '] * 9
            game_active = True
            current_player = 1

# Function for handling the menu
def handle_menu():
    global menu, game_active, menu_active, difficulty, mode, player_symbol, computer_symbol, current_player
    if menu == 1:
        if start_rect.collidepoint(event.pos):
            menu = menu + 1
        if quit_rect.collidepoint(event.pos):
            pygame.quit()
            exit()
    elif menu == 2:
        if pvp_rect.collidepoint(event.pos):
            game_active = True
            menu_active = False
            mode = 1
            menu = menu + 1
        elif pvc_rect.collidepoint(event.pos):
            mode = 2
            menu = menu + 1
    elif menu == 3:
        if no_diff_rect.collidepoint(event.pos):
            menu = menu + 1
            difficulty = '1'
        elif easy_rect.collidepoint(event.pos):
            menu = menu + 1
            difficulty = '2'
        elif normal_rect.collidepoint(event.pos):
            menu = menu + 1
            difficulty = '3'
        elif hard_rect.collidepoint(event.pos):
            menu = menu + 1
            difficulty = '4'
    elif menu == 4:
        if x_rect.collidepoint(event.pos):
            game_active = True
            menu_active = False
            menu = menu + 1
            player_symbol = 'X'
            computer_symbol = 'O'
        elif o_rect.collidepoint(event.pos):
            game_active = True
            menu_active = False
            menu = menu + 1
            player_symbol = 'O'
            computer_symbol = 'X'
            current_player = 2

# Function for handling moves
def handle_moves():
    global board, mode, current_player, computer_symbol, player_symbol
    for i, rect in enumerate(board_rects):
        if mode == 1:
            if rect.collidepoint(event.pos) and board[i] == ' ':
                board[i] = 'X' if current_player == 1 else 'O'
                current_player = 3 - current_player
        if mode == 2:
            if current_player == 1:
                if rect.collidepoint(event.pos) and board[i] == ' ':
                    board[i] = 'X' if player_symbol == 'X' else 'O'
                    current_player = 3 - current_player
                    
    
# Function for handling the escape
def handle_escape():
    global menu, menu_active, game_active
    if menu in [2, 3, 4, 5]:
        if not game_active:
            if not menu_active:
                if menu == 5:
                    menu_active = True
                    reset_board()
                    menu = 4 # Set menu to 5 for choosing the mode
                else:
                    menu_active = True
                    reset_board()
                    menu = 2 # Set menu to 2 for choosing the mode
            else:
                menu -= 1

# Function for handling inputs
def handle_input(event):
    global current_player, game_active, menu_active, menu, mode, difficulty, board
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if game_active:
            handle_moves()      
        else:
            handle_menu()         
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        reset_game()

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        handle_escape()
                        

# Function to check for the winner
def check_winner(board):
    # Check rows
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return board[i]
    # Check columns
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    return None

# Function to search for empty_indices
def empty_indices(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# Function for evaluating the board        
def evaluate(board, depth, player_symbol, opponent):
    winner = check_winner(board)

    if winner == player_symbol:
        return 10 - depth
    elif winner == opponent:
        return depth - 10
    elif ' ' not in board[1:]:
        return 0

# Function for Minimax Algorithm
def minimax(board, depth, maximizingPlayer, player_symbol, opponent):
    if check_winner(board) or ' ' not in board[1:]:
        return evaluate(board, depth, player_symbol, opponent)
    depth += 1

    if maximizingPlayer:
        max_eval = float('-inf')
        for move in empty_indices(board):
            board[move] = player_symbol
            evaluation = minimax(board, depth, False, player_symbol, opponent)
            board[move] = ' '
            max_eval = max(max_eval, evaluation)
        return max_eval
    else:
        min_eval = float('inf')
        for move in empty_indices(board):
            board[move] = opponent
            evaluation = minimax(board, depth, True, player_symbol, opponent)
            board[move] = ' '
            min_eval = min(min_eval, evaluation)
        return min_eval

# Function to get the computer's move in No Diffuclty
def get_random_computer_move(board):
    move = random.choice(empty_indices(board))
    return move

# Function for getting the computer's move in Easy Diffuclty
def get_easy_computer_move(board, opponent):
    # Check if there's a winning move
    for move in empty_indices(board):
        board[move] = opponent
        if check_winner(board):
            board[move] = ' '
            return move
        board[move] = ' '
    # If not, play randomly
    return get_random_computer_move(board)

# Function for getting the computer's move in Normal Difficulty
def get_normal_computer_move(board, player_symbol, opponent):
    # Check if there's a winning or a defensive move
    for symbol in [player_symbol, opponent]:
        for move in empty_indices(board):
            board[move] = symbol
            if check_winner(board):
                board[move] = ' '
                return move
            board[move] = ' '
    # If not, play randomly
    return get_random_computer_move(board)

# Function to get the computer's move in Hard Diffuclty
def get_hard_computer_move(board, player_symbol, opponent):
    # If the board is empty, make a random move
    if len(empty_indices(board)) == 9:
        return get_random_computer_move(board)
    else:
        # Implement the minimax algorithm using the provided logic
        best_move = 0
        best_score = float('-inf')

        for move in empty_indices(board):
            board[move] = player_symbol
            score = minimax(board, 1, False, player_symbol, opponent)
            board[move] = ' '

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

# Function for getting the computer's move
def get_computer_move(board, player_symbol, opponent, difficulty):
    if difficulty == '1':
        return get_random_computer_move(board)
    elif difficulty == '2':
        return get_easy_computer_move(board, opponent)
    elif difficulty == '3':
        return get_normal_computer_move(board, player_symbol, opponent)
    elif difficulty == '4':
        return get_hard_computer_move(board, player_symbol, opponent)
            
pygame.init()
screen = pygame.display.set_mode((450,500))
screen.fill('White')

board_surf = pygame.image.load('graphics/board.png').convert_alpha()
board_rect = board_surf.get_rect(center = (225, 250))

game_font = pygame.font.Font('font/kongtext.ttf', 15)

messages = [
    'Welcome To Tic Tac Toe 2!',
    'Game Version: 1.6',
    'Created By: @Youssef_Bouzidi'
]

winner_messages = ['Player X wins', 'Player O wins', "It's a Tie"]

start_surface = game_font.render('Start', False, 'Black')
start_surface_scaled = pygame.transform.scale2x(start_surface)
start_rect = start_surface_scaled.get_rect(center = (225, 250))

quit_surface = game_font.render('Quit', False, 'Black')
quit_surface_scaled = pygame.transform.scale2x(quit_surface)
quit_rect = quit_surface_scaled.get_rect(center = (225, 295))

mode_surface = game_font.render('Choose The Mode', False, 'Black')
mode_rect = mode_surface.get_rect(center = (225, 200))

pvp_surface = game_font.render('Play with a friend', False, 'Black')
pvp_rect = pvp_surface.get_rect(center = (225, 250))

pvc_surface = game_font.render('Play with a computer', False, 'Black')
pvc_rect = pvc_surface.get_rect(center = (225, 300))
    
difficulty_surf = game_font.render('Choose a difficulty', False, 'Black')
difficulty_rect = difficulty_surf.get_rect(center = (225, 150))

no_diff_surf = game_font.render('Easy', False, 'Black')
easy_surf = game_font.render('Normal', False, 'Black')
normal_surf = game_font.render('Hard', False, 'Black')
hard_surf = game_font.render('Impossible', False, 'Black')


no_diff_rect = no_diff_surf.get_rect(center = (225, 200))
easy_rect = easy_surf.get_rect(center = (225, 250))
normal_rect = normal_surf.get_rect(center = (225, 300))
hard_rect = hard_surf.get_rect(center = (225, 350))

symbols_surf = game_font.render('Choose a smybol', False, 'Black')
x_surf = game_font.render('X', False, 'Black')
o_surf = game_font.render('O', False, 'Black')

symbols_rect = symbols_surf.get_rect(center = (225, 200))
x_rect = x_surf.get_rect(center = (175, 250))
o_rect = x_surf.get_rect(center = (275, 250))

x_symbol = pygame.image.load('graphics/X.png')
o_symbol = pygame.image.load('graphics/O.png')
board_rects = [
    x_symbol.get_rect(center = (120, 362)),
    x_symbol.get_rect(center = (225, 362)),
    x_symbol.get_rect(center = (330, 362)),
    x_symbol.get_rect(center = (120, 258)),
    x_symbol.get_rect(center = (225, 258)),
    x_symbol.get_rect(center = (330, 258)),
    x_symbol.get_rect(center = (120, 152)),
    x_symbol.get_rect(center = (225, 152)),
    x_symbol.get_rect(center = (330, 152)),
]

pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()
current_player = 1
board = [' '] * 9
game_active = False
menu_active = True
menu = 1
mode = 0
difficulty = ''
computer_symbol = ''
player_symbol = ''
thinking_delay = 20

while True:
    for event in pygame.event.get():
        handle_input(event)
    
    if menu_active:
        print_welcome()
        print_menu()
    else:     
        if game_active:
            print_welcome()
            print_board()
            if check_winner(board):
                game_active = False
            elif ' ' not in board[0:]:
                game_active = False
            elif mode == 2 and current_player == 2 and thinking_delay > 0:
                thinking_delay -= 1
            elif mode == 2 and current_player == 2 and thinking_delay == 0:
                if ' ' in board[0:] and not check_winner(board):
                    if computer_symbol == 'O':
                        thinking_delay = 20  # Set the delay to 1 second
                        move = get_computer_move(board, 'O', 'X', difficulty)
                        board[move] = 'O'
                        current_player = 3 - current_player
                    else:
                        thinking_delay = 20  # Set the delay to 1 second
                        move = get_computer_move(board, 'X', 'O', difficulty)
                        board[move] = 'X'
                        current_player = 3 - current_player
        else:
            print_welcome()
            print_winner()
            

    pygame.display.update()
    clock.tick(60)
