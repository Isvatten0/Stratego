import pygame
from checkers.constants import WIDTH, HEIGHT, ROWS, COLS, SQUARE_SIZE
from checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()