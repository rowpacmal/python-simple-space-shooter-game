import pygame
from os import path

# game settings
BACKGROUND_COLOR = (8, 14, 23)
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

# general setup
pygame.init()
pygame.display.set_caption("Space Shooter")
pygame.display.set_icon(pygame.image.load(path.join("src", "images", "player_a.png")))
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
is_running = True

# main game loop
while is_running:
    # event listeners
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # render the game
    display_surface.fill(BACKGROUND_COLOR)
    pygame.display.update()

# clean up
pygame.quit()
exit()
