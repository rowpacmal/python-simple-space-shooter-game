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
is_running, clock = True, pygame.time.Clock()


# load player
player = pygame.image.load(join("src", "images", "player_a.png")).convert_alpha()
player_rect = player.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2()
player_speed = 300


# load laser
laser = pygame.image.load(
    join("src", "images", "player_a_bullet_a.png")
).convert_alpha()
laser_rect = laser.get_frect(topleft=(84, 20))


# load meteor
meteor = pygame.image.load(join("src", "images", "meteor_f.png")).convert_alpha()
meteor_rect = meteor.get_frect(topleft=(20, 20))


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
    # fps
    delta_time = clock.tick() / 1000

    # event listeners
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            is_running = False

    # player inputs
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    player_direction = (
        player_direction.normalize() if player_direction else player_direction
    )
    player_rect.center += player_direction * player_speed * delta_time

    # render the game
    display_surface.fill(BACKGROUND_COLOR)
    for i, pos in enumerate(star_positions):
        display_surface.blit(star_small if i % 2 == 0 else star_large, pos)

    display_surface.blit(meteor, meteor_rect)
    display_surface.blit(laser, laser_rect)
    display_surface.blit(player, player_rect)

    pygame.display.update()


# clean up
pygame.quit()
exit()
