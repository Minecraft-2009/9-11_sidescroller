import pygame

# pygame setup
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 1, 1)
stage_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 0)
clock = pygame.time.Clock()
running = True

velocity = 5

player = pygame.image.load("images_new/plane.png")
player_rect = player.get_rect()
player_rect.centerx = 150
player_rect.centery = 300



# background_rect = background.get_rect()
# background_rect.centerx = 500
# background_rect.centery = 250

# tow = pygame.image.load("images/twin_towers.png")
# towrect = tow.get_rect()
# towrect.centerx = 500
# towrect.centery = 300

def player_move(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and self.y >= 10:
        self.y -= velocity
    if keys[pygame.K_DOWN] and self.y <= WINDOW_HEIGHT-100:
        self.y += velocity


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, typ3): 
        super().__init__() 
        self.image = pygame.image.load(f"images_new/{typ3}.png")
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        

        self.rect.bottomleft = (self.x, self.y)

    # def tower_blit(self):
    #     display_surface.blit(self.image, self.rect)

    def update(self):
        self.x -= 1
        self.rect.bottomleft = (self.x, self.y)


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y,): 
        super().__init__() 
        self.image = pygame.image.load(f"backgrounds/skyline.png")
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.bottomleft = (x, y)
    
    def update(self):
        self.x -= 1
        self.rect.bottomleft = (self.x, self.y)
        if self.x == -2250:
            self.x = 0


tow = Obstacle(767, WINDOW_HEIGHT, "twin_towers")
tow1 = Obstacle(1400, WINDOW_HEIGHT, "twin_towers")
tow3 = Obstacle(1300, 200, "spy_balloon")
stage = Background(0, 500)

level_1_group = pygame.sprite.Group()
level_1_group.add(tow)
level_1_group.add(tow1)
level_1_group.add(tow3)


stage_group = pygame.sprite.GroupSingle()
stage_group.add(stage)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player_move(player_rect)
    stage_group.update()
    stage_group.draw(stage_surface)
    # fill the display_surface with a color to wipe away anything from last frame
    # display_surface.fill("lightblue")
    display_surface.blit(player, player_rect)

    #stage_surface.fill("white")
    #stage_surface.blit(f"backgrounds/skyline.png")

    level_1_group.update()
    level_1_group.draw(display_surface)
    
    # collision logic
    # if player_rect.colliderect()

    player_move(player_rect)

    # display_surface.blit(tow, towrect)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on display_surface

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()