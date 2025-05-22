import pygame
from os.path import join
from random import randint


# game settings
BACKGROUND_COLOR = (8, 14, 23)
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720


# sprites
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.image.load(
            join("src", "images", "player_a.png")
        ).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.is_shooting = False
        self.shoot_time = 0
        self.cooldown_duration = 400

    def shoot_timer(self):
        if self.is_shooting:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.cooldown_duration:
                self.is_shooting = False

    def update(self, delta_time):
        self.player_move(delta_time)
        self.player_shoot()

    def player_move(self, delta_time):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = (
            self.direction.normalize() if self.direction else self.direction
        )
        self.rect.center += self.direction * self.speed * delta_time

    def player_shoot(self):
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and not self.is_shooting:
            Laser(all_sprites, laser, self.rect.midtop)
            self.is_shooting = True
            self.shoot_time = pygame.time.get_ticks()
        self.shoot_timer()


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, image, position):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(midbottom=position)
        self.speed = 400

    def update(self, delta_time):
        self.rect.centery -= self.speed * delta_time
        if self.rect.bottom < 0:
            self.kill()


class Star(pygame.sprite.Sprite):
    def __init__(self, groups, image):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(
            center=(randint(0, WINDOW_WIDTH - 64), randint(0, WINDOW_HEIGHT - 64))
        )


# general setup
pygame.init()
pygame.display.set_caption("Space Shooter")
pygame.display.set_icon(pygame.image.load(join("src", "images", "player_a.png")))
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
is_running, clock = True, pygame.time.Clock()


# asset imports
star_a = pygame.image.load(join("src", "images", "star_a.png")).convert_alpha()
star_b = pygame.image.load(join("src", "images", "star_b.png")).convert_alpha()
star_a.set_alpha(50), star_b.set_alpha(50)
laser = pygame.image.load(
    join("src", "images", "player_a_bullet_a.png")
).convert_alpha()

# sprite groups
all_sprites = pygame.sprite.Group()


# create sprites
for i in range(20):
    Star(all_sprites, star_a) if i % 2 == 0 else Star(all_sprites, star_b)
player = Player(all_sprites)


# load meteor
meteor = pygame.image.load(join("src", "images", "meteor_f.png")).convert_alpha()
meteor_rect = meteor.get_frect(topleft=(20, 20))

# custom events
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 1000)


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
        if event.type == meteor_event:
            # print("meteor!")
            pass

    # update sprites
    all_sprites.update(delta_time)

    # render game
    display_surface.fill(BACKGROUND_COLOR)
    all_sprites.draw(display_surface)

    # update display
    pygame.display.update()


# clean up
pygame.quit()
exit()
