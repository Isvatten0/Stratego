import pygame

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Your game logic and drawing code here

    pygame.display.flip()  # Update the display

pygame.quit()  # Quit Pygame when done
