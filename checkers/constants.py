import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
BOMB_BLUE = pygame.transform.scale(pygame.image.load('assets/Bomb_Blue.png'), (48, 64))
BOMB_RED = pygame.transform.scale(pygame.image.load('assets/Bomb_Red.png'), (48, 64))