import pygame
from os.path import join
from random import randint


# game settings
BACKGROUND_COLOR = (8, 14, 23)
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720


# general setup
pygame.init()
pygame.display.set_caption("Space Shooter")
pygame.display.set_icon(pygame.image.load(join("src", "images", "player_a.png")))
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
is_running = True


# load assets
player = pygame.image.load(join("src", "images", "player_a.png")).convert_alpha()
x, y = 100, 150

# load stars
star_small = pygame.image.load(join("src", "images", "star_a.png")).convert_alpha()
star_large = pygame.image.load(join("src", "images", "star_b.png")).convert_alpha()
star_small.set_alpha(50)
star_large.set_alpha(50)
star_positions = [
    (randint(0, WINDOW_WIDTH - 64), randint(0, WINDOW_HEIGHT - 64)) for _ in range(20)
]


# main game loop
while is_running:
    # event listeners
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # render the game
    display_surface.fill(BACKGROUND_COLOR)
    for i, pos in enumerate(star_positions):
        display_surface.blit(star_small if i % 2 == 0 else star_large, pos)

    x += 0.1
    display_surface.blit(player, (x, y))
    pygame.display.update()


# clean up
pygame.quit()
exit()
