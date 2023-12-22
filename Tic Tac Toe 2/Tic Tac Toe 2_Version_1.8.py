# Tic-Tac-Toe 2!
# Game Version: 1.8
# The Display Update! What's new ?:
# added wins loses and draw display to the end of the game

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
        screen.blit(cvc_surface, cvc_rect)
    if mode == 2:
        if menu == 3:
            screen.blit(difficulty_surf, difficulty_rect)
            screen.blit(no_diff_surf, no_diff_rect)
            screen.blit(easy_surf, easy_rect)
            screen.blit(normal_surf, normal_rect)
            screen.blit(hard_surf, hard_rect)
        elif menu == 4:
            screen.blit(symbols_surf, symbols_rect)
            screen.blit(x_surf, x_rect)
            screen.blit(o_surf, o_rect)
    elif mode == 3:
        if menu == 3:
            screen.blit(choose_diff_surf, choose_diff_rect)
            screen.blit(computer_x_diff_surf, computer_x_diff_rect)
            screen.blit(no_diff_surf, no_diff_rect)
            screen.blit(easy_surf, easy_rect)
            screen.blit(normal_surf, normal_rect)
            screen.blit(hard_surf, hard_rect)
        elif menu == 4:
            screen.blit(choose_diff_surf, choose_diff_rect)
            screen.blit(computer_o_diff_surf, computer_o_diff_rect)
            screen.blit(no_diff_surf, no_diff_rect)
            screen.blit(easy_surf, easy_rect)
            screen.blit(normal_surf, normal_rect)
            screen.blit(hard_surf, hard_rect)
            
        
    
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
    #(screen_x_centre, screen_y_centre + 180)
    #(screen_x_centre, screen_y_pos - 70)
    message_rect = message_surface_scaled.get_rect(center = (screen_x_centre, screen_y_centre + 180))
    screen.blit(message_surface_scaled, message_rect)

    instruction_message = game_font.render('Press Space to retry', False, 'Black')
    #(screen_x_centre, screen_y_centre + 215)
    #(screen_x_centre, screen_y_pos - 25)
    instruction_message_rect = instruction_message.get_rect(center = (screen_x_centre, screen_y_centre + 215))
    screen.blit(instruction_message, instruction_message_rect)

# Functionf for printing the score
def display_score():
    global mode, total_wins
    if mode == 1:
        win_surf = game_font.render('Player X: [ {} ]'.format(total_wins['X']), False, 'Black')
        win_rect = win_surf.get_rect(center = (screen_x_centre - 300, screen_y_pos - 25))
        screen.blit(win_surf,win_rect)
        
        loses_surf = game_font.render('Player O: [ {} ]'.format(total_wins['O']), False, 'Black')
        loses_rect = loses_surf.get_rect(center = (screen_x_centre, screen_y_pos - 25))
        screen.blit(loses_surf,loses_rect)
        
        draw_surf = game_font.render('Draws: [ {} ]'.format(total_wins[' ']), False, 'Black')
        draw_rect = draw_surf.get_rect(center = (screen_x_centre + 300, screen_y_pos - 25))
        screen.blit(draw_surf, draw_rect)
    elif mode == 2:
        if player_symbol == 'X':
            win_surf = game_font.render('Wins: [ {} ]'.format(total_wins['O']), False, 'Black')
        else:
            win_surf = game_font.render('Wins: [ {} ]'.format(total_wins['X']), False, 'Black')
            
        win_rect = win_surf.get_rect(center = (screen_x_centre - 300, screen_y_pos - 25))
        screen.blit(win_surf,win_rect)

        if player_symbol == 'X':
            loses_surf = game_font.render('Loses: [ {} ]'.format(total_wins['X']), False, 'Black')
        else:
            loses_surf = game_font.render('Loses: [ {} ]'.format(total_wins['O']), False, 'Black')
            
        loses_rect = loses_surf.get_rect(center = (screen_x_centre, screen_y_pos - 25))
        screen.blit(loses_surf,loses_rect)
            
        draw_surf = game_font.render('Draws: [ {} ]'.format(total_wins[' ']), False, 'Black')
        draw_rect = draw_surf.get_rect(center = (screen_x_centre + 300, screen_y_pos - 25))
        screen.blit(draw_surf, draw_rect)
    elif mode == 3:
        win_surf = game_font.render('Computer X: [ {} ]'.format(total_wins['X']), False, 'Black')
        win_rect = win_surf.get_rect(center = (screen_x_centre - 300, screen_y_pos - 25))
        screen.blit(win_surf, win_rect)
        
        loses_surf = game_font.render('Computer O: [ {} ]'.format(total_wins['O']), False, 'Black')
        loses_rect = loses_surf.get_rect(center = (screen_x_centre, screen_y_pos - 25))
        screen.blit(loses_surf, loses_rect)
        
        draw_surf = game_font.render('Draws: [ {} ]'.format(total_wins[' ']), False, 'Black')
        draw_rect = draw_surf.get_rect(center = (screen_x_centre + 300, screen_y_pos - 25))
        screen.blit(draw_surf, draw_rect)
    
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
            if mode == 2 and player_symbol == 'O':
                current_player = 2
            else:
                current_player = 1

# Function for handling menu 1
def handle_menu_1():
    global menu
    if start_rect.collidepoint(event.pos):
            menu = menu + 1
    elif quit_rect.collidepoint(event.pos):
        pygame.quit()
        exit()

# Function for handling menu 2
def handle_menu_2():
    global menu, game_active, menu_active, mode
    if pvp_rect.collidepoint(event.pos):
        game_active = True
        menu_active = False
        mode = 1
        menu = menu + 1
    elif pvc_rect.collidepoint(event.pos):
        mode = 2
        menu = menu + 1
    elif cvc_rect.collidepoint(event.pos):
        mode = 3
        menu = menu + 1
    
    
# Function for handling menu 3
def handle_menu_3():
    global menu, difficulty, mode, computer_x_diff
    if mode == 2:
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
    elif mode == 3:
        if no_diff_rect.collidepoint(event.pos):
            menu = menu + 1
            computer_x_diff = '1'
        elif easy_rect.collidepoint(event.pos):
            menu = menu + 1
            computer_x_diff = '2'
        elif normal_rect.collidepoint(event.pos):
            menu = menu + 1
            computer_x_diff = '3'
        elif hard_rect.collidepoint(event.pos):
            menu = menu + 1
            computer_x_diff = '4'


# Function for handling the menu 4
def handle_menu_4():
    global menu, game_active, menu_active, difficulty, mode, player_symbol, computer_symbol, current_player, computer_o_diff, computer_x_diff
    if mode == 2:
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
    elif mode == 3:
        if no_diff_rect.collidepoint(event.pos):
            game_active = True
            menu_active = False
            menu = menu + 1
            computer_o_diff = '1'
        elif easy_rect.collidepoint(event.pos):
            game_active = True
            menu_active = False
            menu = menu + 1
            computer_o_diff = '2'
        elif normal_rect.collidepoint(event.pos):
            game_active = True
            menu_active = False
            menu = menu + 1
            computer_o_diff = '3'
        elif hard_rect.collidepoint(event.pos):
            game_active = True
            menu_active = False
            menu = menu + 1
            computer_o_diff = '4'
    
    
# Function for handling the menu
def handle_menu():
    global menu
    if menu == 1:
        handle_menu_1()
    elif menu == 2:
        handle_menu_2()  
    elif menu == 3:
        handle_menu_3()
    elif menu == 4:
        handle_menu_4()

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
    global menu, menu_active, game_active, total_wins
    if menu in [2, 3, 4, 5]:
        if not game_active:
            if not menu_active:
                if menu == 5:
                    menu_active = True
                    reset_board()
                    total_wins = {'X': 0, 'O': 0, ' ': 0} # reset the total wins counter
                    menu = 4 # Set menu to 5 for choosing the mode
                else:
                    menu_active = True
                    reset_board()
                    total_wins = {'X': 0, 'O': 0, ' ': 0} # reset the total wins counter
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
screen_x_pos = 900
screen_y_pos = 600
screen_x_centre = screen_x_pos / 2
screen_y_centre = screen_y_pos / 2

screen = pygame.display.set_mode((screen_x_pos,screen_y_pos))
screen.fill('White')

board_surf = pygame.image.load('graphics/board.png').convert_alpha()
board_rect = board_surf.get_rect(center = (screen_x_centre, screen_y_centre))

game_font = pygame.font.Font('font/kongtext.ttf', 15)

messages = [
    'Welcome To Tic Tac Toe 2!',
    'Game Version: 1.8',
    'Created By: @Youssef_Bouzidi'
]

winner_messages = ['Player X wins', 'Player O wins', "It's a Tie"]

start_surface = game_font.render('Start', False, 'Black')
start_surface_scaled = pygame.transform.scale2x(start_surface)
start_rect = start_surface_scaled.get_rect(center = (screen_x_centre, screen_y_centre))

quit_surface = game_font.render('Quit', False, 'Black')
quit_surface_scaled = pygame.transform.scale2x(quit_surface)
quit_rect = quit_surface_scaled.get_rect(center = (screen_x_centre, screen_y_centre + 65))

mode_surface = game_font.render('Choose The Mode', False, 'Black')
mode_y_pos = screen_y_centre - 50
mode_rect = mode_surface.get_rect(center = (screen_x_centre, mode_y_pos))

pvp_surface = game_font.render('Play with a friend', False, 'Black')
pvp_rect = pvp_surface.get_rect(center = (screen_x_centre, mode_y_pos + 50))

pvc_surface = game_font.render('Play with a computer', False, 'Black')
pvc_rect = pvc_surface.get_rect(center = (screen_x_centre, mode_y_pos + 100))

cvc_surface = game_font.render('Simulate a Game', False, 'Black')
cvc_rect = cvc_surface.get_rect(center = (screen_x_centre, mode_y_pos + 150))

difficulty_surf = game_font.render('Choose a difficulty', False, 'Black')
diff_y_pos = mode_y_pos - 50
difficulty_rect = difficulty_surf.get_rect(center = (screen_x_centre, diff_y_pos))

choose_diff_surf = game_font.render('Choose The difficulty for', False, 'Black')
computer_x_diff_surf = game_font.render('Computer X', False, 'Black')
computer_o_diff_surf = game_font.render('Computer O', False, 'Black')

choose_diff_rect = choose_diff_surf.get_rect(center = (screen_x_centre, diff_y_pos - 20))
computer_x_diff_rect = computer_x_diff_surf.get_rect(center = (screen_x_centre + 10, diff_y_pos + 10))
computer_o_diff_rect = computer_o_diff_surf.get_rect(center = (screen_x_centre + 10, diff_y_pos + 10))

no_diff_surf = game_font.render('Easy', False, 'Black')
easy_surf = game_font.render('Normal', False, 'Black')
normal_surf = game_font.render('Hard', False, 'Black')
hard_surf = game_font.render('Impossible', False, 'Black')


no_diff_rect = no_diff_surf.get_rect(center = (screen_x_centre, diff_y_pos + 50))
easy_rect = easy_surf.get_rect(center = (screen_x_centre, diff_y_pos + 100))
normal_rect = normal_surf.get_rect(center = (screen_x_centre, diff_y_pos + 150))
hard_rect = hard_surf.get_rect(center = (screen_x_centre, diff_y_pos + 200))

symbols_surf = game_font.render('Choose a smybol', False, 'Black')
x_surf = game_font.render('X', False, 'Black')
o_surf = game_font.render('O', False, 'Black')

symbols_rect = symbols_surf.get_rect(center = (screen_x_centre, mode_y_pos))
x_rect = x_surf.get_rect(center = (screen_x_centre - 50, mode_y_pos + 50))
o_rect = x_surf.get_rect(center = (screen_x_centre + 50, mode_y_pos + 50))

x_symbol = pygame.image.load('graphics/X.png')
o_symbol = pygame.image.load('graphics/O.png')
board_rects = [
    x_symbol.get_rect(center = (screen_x_centre - 105, (screen_y_centre + 105) + 8)),
    x_symbol.get_rect(center = (screen_x_centre, (screen_y_centre + 105) + 8)),
    x_symbol.get_rect(center = (screen_x_centre + 105, (screen_y_centre + 105) + 8)),
    x_symbol.get_rect(center = (screen_x_centre - 105, screen_y_centre + 8)),
    x_symbol.get_rect(center = (screen_x_centre, screen_y_centre + 8)),
    x_symbol.get_rect(center = (screen_x_centre + 105, screen_y_centre + 8)),
    x_symbol.get_rect(center = (screen_x_centre - 105, (screen_y_centre - 105) + 8)),
    x_symbol.get_rect(center = (screen_x_centre, (screen_y_centre - 105) + 8)),
    x_symbol.get_rect(center = (screen_x_centre + 105, (screen_y_centre - 105) + 8)),
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
computer_x_diff = ''
computer_o_diff = ''
total_wins = {'X': 0, 'O': 0, ' ': 0}

while True:
    for event in pygame.event.get():
        handle_input(event)
    
    if menu_active:
        print_welcome()
        print_menu()
    else:     
        if game_active:
            wins = {'X': 0, 'O': 0, ' ': 0}
            print_welcome()
            print_board()
            if mode == 2:
                player = player_symbol if current_player == 1 else computer_symbol
            else:
                player = 'O' if current_player == 1 else 'X'
                
            if check_winner(board):
                game_active = False
                wins[player] += 1
            elif ' ' not in board[0:]:
                game_active = False
                wins[' '] += 1
            elif mode == 2 and current_player == 2 and thinking_delay > 0:
                thinking_delay -= 1
            elif mode == 2 and current_player == 2 and thinking_delay == 0:
                if ' ' in board[0:] and not check_winner(board):
                    if computer_symbol == 'O':
                        thinking_delay = 20  # Set a delay of 20 game loops before making a move.
                        move = get_computer_move(board, 'O', 'X', difficulty)
                        board[move] = 'O'
                        current_player = 3 - current_player
                    else:
                        thinking_delay = 20  # Set a delay of 20 game loops before making a move.
                        move = get_computer_move(board, 'X', 'O', difficulty)
                        board[move] = 'X'
                        current_player = 3 - current_player
            elif mode == 3 and thinking_delay > 0:
                thinking_delay -= 1
            elif mode == 3 and thinking_delay == 0:
                if ' ' in board[0:] and not check_winner(board):
                    if current_player == 1:
                        difficulty = computer_x_diff
                        thinking_delay = 20  # Set a delay of 20 game loops before making a move.
                        move = get_computer_move(board, 'X', 'O', difficulty)
                        board[move] = 'X'
                        current_player = 3 - current_player
                    else:
                        difficulty = computer_o_diff
                        thinking_delay = 20  # Set a delay of 20 game loops before making a move.
                        move = get_computer_move(board, 'O', 'X', difficulty)
                        board[move] = 'O'
                        current_player = 3 - current_player
                        
            total_wins['X'] += wins['X']
            total_wins['O'] += wins['O']
            total_wins[' '] += wins[' ']
            
        else:
            print_welcome()
            print_winner()
            display_score()
            

    pygame.display.update()
    clock.tick(60)
