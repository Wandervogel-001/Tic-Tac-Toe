# Tic-Tac-Toe 2!
# Game Version: 1.1
# The GUI Update! What's new ?:
# changed the winner display


import pygame
import random
import time
from sys import exit


# Function for drawing the board
def draw_board():
    screen.fill('White')
    screen.blit(board_surf, board_rect)
    for i, message in enumerate(messages):
        text_surface = game_font.render(message, False, 'Black')
        text_rect = text_surface.get_rect(topleft=(5, 5 + i * 20))
        screen.blit(text_surface, text_rect)
    for i, symbol in enumerate(board):
        if symbol == 'X':
            screen.blit(x_symbol, board_rects[i])
        elif symbol == 'O':
            screen.blit(o_symbol, board_rects[i])

# Function for drawing the outro screen
def draw_outro():
    draw_board()
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


# Function for resting the game
def reset_game():
    global board, game_active, current_player
    board = [' '] * 9
    game_active = True
    current_player = 1


# Function for handling inputs
def handle_input():
    global current_player, game_active
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_active:
                for i, rect in enumerate(board_rects):
                    if rect.collidepoint(event.pos) and board[i] == ' ':
                        board[i] = 'X' if current_player == 1 else 'O'
                        current_player = 3 - current_player
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reset_game()


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
            
pygame.init()
screen = pygame.display.set_mode((450,500))

board_surf = pygame.image.load('graphics/board.png').convert_alpha()
board_rect = board_surf.get_rect(center = (225, 250))

game_font = pygame.font.Font('font/kongtext.ttf', 15)

messages = [
    'Welcome To Tic Tac Toe 2!',
    'Game Version: 1.1',
    'Created By: @Youssef_Bouzidi'
]

winner_messages = ['Player X wins', 'Player O wins', "It's a Tie"]

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
game_active = True

while True:
    handle_input()

    if game_active:
        draw_board()
        if check_winner(board):
            game_active = False
            current_player = 1
        if ' ' not in board[0:]:
            game_active = False
            current_player = 1
    else:
        draw_outro()

    pygame.display.update()
    clock.tick(60)
