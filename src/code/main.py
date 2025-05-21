import pygame

# general setup
pygame.init()
BACKGROUND_COLOR = (8, 14, 23)
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
pygame.display.set_icon(pygame.image.load("src/images/player_a.png"))
is_running = True

while is_running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # render the game
    display_surface.fill(BACKGROUND_COLOR)
    pygame.display.update()

pygame.quit()
exit()
