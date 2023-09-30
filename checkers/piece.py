import pygame

from .constants import RED, WHITE, SQUARE_SIZE, GRAY, CROWN,BOMB_RED,BOMB_BLUE

class Piece:
    PADDING = 15
    BORDER = 2
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = True

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        # radius = SQUARE_SIZE // 2 - self.PADDING
        # pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.BORDER)
        # pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king and self.color == "Blue":
            win.blit(BOMB_BLUE, (self.x - BOMB_BLUE.get_width() // 2, self.y - BOMB_BLUE.get_height() // 2))
        else:
            win.blit(BOMB_RED, (self.x - BOMB_RED.get_width() // 2, self.y - BOMB_RED.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)