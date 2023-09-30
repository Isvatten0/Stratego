import pygame

WIDTH, HEIGHT = 700, 700
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//COLS

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
BOMB_BLUE = pygame.transform.scale(pygame.image.load('assets/Bomb_Blue.png'), (48, 64))
BOMB_RED = pygame.transform.scale(pygame.image.load('assets/Bomb_Red.png'), (48, 64))
CAPTAIN_BLUE = pygame.transform.scale(pygame.image.load('assets/Captain_Blue.png'), (48, 64))
CAPTAIN_RED = pygame.transform.scale(pygame.image.load('assets/Captain_Red.png'), (48, 64))
SCOUT_BLUE = pygame.transform.scale(pygame.image.load('assets/Scout_Blue.png'), (48, 64))
SCOUT_RED = pygame.transform.scale(pygame.image.load('assets/Scout_Red.png'), (48, 64))
SERGEANT_BLUE = pygame.transform.scale(pygame.image.load('assets/Sergeant_Blue.png'), (48, 64))
SERGEANT_RED = pygame.transform.scale(pygame.image.load('assets/Sergeant_Red.png'), (48, 64))
MINER_BLUE = pygame.transform.scale(pygame.image.load('assets/Miner_Blue.png'), (48, 64))
MINER_RED = pygame.transform.scale(pygame.image.load('assets/Miner_Red.png'), (48, 64))
COLONEL_BLUE = pygame.transform.scale(pygame.image.load('assets/Colonel_Blue.png'), (48, 64))
COLONEL_RED = pygame.transform.scale(pygame.image.load('assets/Colonel_Red.png'), (48, 64))
LIEUTENANT_BLUE = pygame.transform.scale(pygame.image.load('assets/Lieutenant_Blue.png'), (48, 64))
LIEUTENANT_RED = pygame.transform.scale(pygame.image.load('assets/Lieutenant_Red.png'), (48, 64))
MAJOR_BLUE = pygame.transform.scale(pygame.image.load('assets/Major_Blue.png'), (48, 64))
MAJOR_RED = pygame.transform.scale(pygame.image.load('assets/Major_Red.png'), (48, 64))
GENERAL_BLUE = pygame.transform.scale(pygame.image.load('assets/General_Blue.png'), (48, 64))
GENERAL_RED = pygame.transform.scale(pygame.image.load('assets/General_Red.png'), (48, 64))
MARSHAL_BLUE = pygame.transform.scale(pygame.image.load('assets/Marshal_Blue.png'), (48, 64))
MARSHAL_RED = pygame.transform.scale(pygame.image.load('assets/Marshal_Red.png'), (48, 64))
FLAG_BLUE = pygame.transform.scale(pygame.image.load('assets/Flag_Blue.png'), (48, 64))
FLAG_RED = pygame.transform.scale(pygame.image.load('assets/Flag_Red.png'), (48, 64))
SPY_BLUE = pygame.transform.scale(pygame.image.load('assets/Spy_Blue.png'), (48, 64))
SPY_RED = pygame.transform.scale(pygame.image.load('assets/Spy_Red.png'), (48, 64))