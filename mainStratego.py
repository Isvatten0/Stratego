import pygame
from Stratego.constants import WIDTH, HEIGHT, ROWS, COLS, SQUARE_SIZE
from checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Stratego')
background_image = pygame.image.load("stratego.png")  # Replace "background.jpg" with your image file path
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    # board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            
            # Blit the background image onto the screen
        WIN.blit(background_image, (0, 0))

        # board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()