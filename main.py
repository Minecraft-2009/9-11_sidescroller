import pygame, pickle

# pygame setup
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 1, 1)
# stage_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 0)
clock = pygame.time.Clock()
running = True

# menu positions
menu_topleft = (WINDOW_WIDTH//5, WINDOW_HEIGHT//4)
menu_topright = (4*(WINDOW_WIDTH//5), WINDOW_HEIGHT//4)
menu_bottomleft = (WINDOW_WIDTH//5, 3*(WINDOW_HEIGHT//4))
menu_bottomright = (4*(WINDOW_WIDTH//5)), (3*(WINDOW_HEIGHT//4))

# print(WINDOW_WIDTH//5+(3*WINDOW_WIDTH//5))
#     #    2*WINDOW_HEIGHT//4)

menu_exit_image = pygame.image.load("images.old/menu_exit.png")
menu_exit_rect = menu_exit_image.get_rect()
menu_exit_rect.topright = (menu_topright[0]-2, menu_topright[1] +2)


plane_velocity = 5

font_start = pygame.font.SysFont("arial", 32, True)
font_start_s = pygame.font.SysFont("arial", 28, True)

start_text = font_start.render('SELECT LEVEL', True, (0,0,0),(68,149,212))
start_rect = start_text.get_rect()
start_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//5)

player = pygame.image.load("images.old/b-767.png")
player_rect = player.get_rect()
player_rect.centerx = 150
player_rect.centery = 300

is_paused_button = pygame.image.load("images.old/playing_game.png")
is_paused_button_rect = is_paused_button.get_rect()
is_paused_button_rect.topright = (WINDOW_WIDTH, 0)

# level images
level_1_image = pygame.image.load("level_images/level_1_selection.png")
level_1_image_rect = level_1_image.get_rect()
level_1_image_rect.topleft = (32, WINDOW_HEIGHT//4)

level_2_image = pygame.image.load("level_images/level_1_selection.png")
level_2_image_rect = level_2_image.get_rect()
level_2_image_rect.topleft = (level_1_image_rect.topright[0]+16, WINDOW_HEIGHT//4)


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
        self.y -= plane_velocity
    if keys[pygame.K_DOWN] and self.y <= WINDOW_HEIGHT-100:
        self.y += plane_velocity

# PICKLE
levels_unlocked_path = "levels_unlocked.pickle"
def pickle_dump(file, file_path):
        # Open the file in binary mode
    # with open(file_path, 'wb') as file:
    #     # Serialize and write the variable to the file
    #     pickle.dump(file_path, file)
    with open(file_path, 'wb') as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # Step 3: Loading Variables
    # loaded_data = None
def pickle_get(file_path):
    with open(file_path, 'rb') as file:
    # Deserialize and retrieve the variable from the file
        return pickle.load(file)

levels_unlocked = []
# pickle_dump(levels_unlocked, levels_unlocked_path)

# levels_unlocked_py = []
levels_unlocked = pickle_get(levels_unlocked_path)
print(levels_unlocked)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, velo, typ3): 
        super().__init__() 
        self.image = pygame.image.load(f"images.old/{typ3}.png")
        self.rect = self.image.get_rect()
        self.velocity = velo

        self.is_player_dead = False

        self.x = x
        self.y = y
        

        self.rect.bottomleft = (self.x, self.y)

    # def tower_blit(self):
    #     display_surface.blit(self.image, self.rect)
    def check_collision(self):
        if self.rect.colliderect(player_rect):
            return True

    def update(self):
        self.x -= self.velocity
        self.rect.bottomleft = (self.x, self.y)
        if self.check_collision():
            # print('YOU DIED')
            self.is_player_dead = True   


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y,): 
        super().__init__() 
        self.image = pygame.image.load(f"backgrounds/skyline_clear.png")
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.bottomleft = (x, y)
    

    def update(self):
        self.x -= 1
        self.rect.bottomleft = (self.x, self.y)
        if self.x == -2000:
            self.x = 0
        

class LevelEnd(pygame.sprite.Sprite):
    def __init__(self, x, velo): 
        super().__init__() 
        self.x = x
        self.velocity = velo
        self.image = pygame.image.load("level_end.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, 0)    

    def update(self):
        self.x -= self.velocity
        self.rect.topleft = (self.x, 0)    

stage = Background(0, 500)
stage_group = pygame.sprite.GroupSingle()
stage_group.add(stage)

player_just_died = False
death_congratulations_text = font_start_s.render('HA LOSER!!', True, (255,0,0),(68,149,212))
death_congratulations_rect = death_congratulations_text.get_rect()
death_congratulations_rect.centerx = WINDOW_WIDTH//2
death_congratulations_rect.centery = 32

playing = False
paused = False
level_1 = False
level_1_init = False
level_1_available = True
level_2 = False
level_2_init = False
level_2_available = False



while running:
    # Level 1
    if level_1_init:
        tow = Obstacle(767, WINDOW_HEIGHT, 3, "twin_towers")
        tow1 = Obstacle(1400, WINDOW_HEIGHT, 3, "twin_towers")
        tow2 = Obstacle(1300, 200, 3, "balloon")
        tow3 = Obstacle(1930,370, 3, "malaysia_370")
        tow4 = Obstacle(1970,223, 3, "malaysia_370")
        tow5 = Obstacle(1945, WINDOW_HEIGHT, 3, "panzer")
        tow6 = Obstacle(2700, WINDOW_HEIGHT, 3, "twin_towers")
        tow7 = Obstacle(2600, 100, 3, "malaysia_370")
        # wolter = Obstacle(3000, WINDOW_HEIGHT, "walt2")
        level_1_group = pygame.sprite.Group()
        level_1_group.add(tow)
        level_1_group.add(tow1)
        level_1_group.add(tow2)
        level_1_group.add(tow3)
        level_1_group.add(tow4)
        level_1_group.add(tow5)
        level_1_group.add(tow6)
        level_1_group.add(tow7)
        # level_1_group.add(wolter)

        level_1_end = LevelEnd(3000, 3)
        level_1_end_group = pygame.sprite.Group()
        level_1_end_group.add(level_1_end)

        level_1 = True
        level_1_init = False
    if level_2_init:
        t2t1 = Obstacle(767, WINDOW_HEIGHT, 3, "twin_towers")
        t2t2 = Obstacle(1300, 185, 3, "malaysia_370")
        t2t3 = Obstacle(1500, WINDOW_HEIGHT-40, 3, "panzer")
        t2t4= Obstacle(1300, 400, 3, "pigeon")
        t2t5 = Obstacle(1900, 400, 3, "balloon")
        t2t6 = Obstacle(1700, 300, 3, "balloon")
        disseaparing_t2t7 = Obstacle(1200, 60, 3, "pigeon")
        t2t8 = Obstacle(2350, 175, 3, "valter_vite")
        disseaparing_t2t9 = Obstacle(4500, 400, 7, "missile")

        level_2_group = pygame.sprite.Group()
        level_2_group.add(t2t1)
        level_2_group.add(t2t2)
        level_2_group.add(t2t3)
        level_2_group.add(t2t4)
        level_2_group.add(t2t5)
        level_2_group.add(t2t6)
        level_2_group.add(disseaparing_t2t7)
        level_2_group.add(t2t8)
        level_2_group.add(disseaparing_t2t9)

        level_2 = True
        level_2_init = False


    for lev in levels_unlocked:
        if lev == 1:
            level_1_available = True
        if lev == 2:
            level_2_available = True



    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_ESCAPE]:
            running = False
        if playing:
            player_move(player_rect)
        if not paused:
            if keys[pygame.K_p]:
                paused = True
                # print("paused")
                is_paused_button = pygame.image.load("images.old/paused_game.png")
                is_paused_button_rect = is_paused_button.get_rect()
                is_paused_button_rect.topright = (WINDOW_WIDTH, 0)
                continue
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and is_paused_button_rect.collidepoint(mouse_pos):
                paused = True
                # print("paused")
                is_paused_button = pygame.image.load("images.old/paused_game.png")
                is_paused_button_rect = is_paused_button.get_rect()
                is_paused_button_rect.topright = (WINDOW_WIDTH, 0)
                continue
        if paused:
            if keys[pygame.K_o]:
                paused = False
                is_paused_button = pygame.image.load("images.old/playing_game.png")
                is_paused_button_rect = is_paused_button.get_rect()
                is_paused_button_rect.topright = (WINDOW_WIDTH, 0)
                # print("unpaused")
                continue
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                # if mouse_pos[0] >= WINDOW_WIDTH//2:
                if menu_exit_rect.collidepoint(mouse_pos):
                    paused = False
              
    if not playing:
        display_surface.fill((68,149,212))
        if player_just_died:
            display_surface.blit(death_congratulations_text, death_congratulations_rect)
            # print("blit death")
        display_surface.blit(start_text, start_rect)
        if level_1_available:
            display_surface.blit(level_1_image, level_1_image_rect)
        if level_2_available:
            display_surface.blit(level_2_image, level_2_image_rect)
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            # if mouse_pos[0] >= WINDOW_WIDTH//2:
            if level_1_image_rect.collidepoint(mouse_pos):
                player_just_died = False
                playing = True
                level_1_init = True
            if level_2_image_rect.collidepoint(mouse_pos):
                player_just_died = False
                playing = True
                level_2_init = True

    if playing:
        if not paused:
            stage_group.update()
            stage_group.draw(display_surface)
            # fill the display_surface with a color to wipe away anything from last frame
            # display_surface.fill("lightblue")
            display_surface.blit(player, player_rect)

            #stage_surface.fill("white")
            #stage_surface.blit(f"backgrounds/skyline.png")
            if level_1:
                for obs in level_1_group:
                    if obs.is_player_dead:
                        # print("PLAYER DEAD")
                        player_just_died = True
                        playing = False
                        for sui in level_1_group:
                            sui.kill()
                level_1_end_group.update()
                level_1_end_group.draw(display_surface)
                level_1_group.update()
                level_1_group.draw(display_surface)
                if player_rect.colliderect(level_1_end.rect):
                    if not level_2_available:
                        levels_unlocked.append(2)
                        pickle_dump(levels_unlocked, levels_unlocked_path)

                    level_2_init = True
                    level_1 = False
            
            if level_2:
                level_2_available = True
                for obs in level_2_group:
                    if obs.is_player_dead:
                        # print("PLAYER DEAD")
                        player_just_died = True
                        playing = False
                        for sui in level_2_group:
                            sui.kill()
                # dissapearing blocks
                if disseaparing_t2t7.x <= 300:
                    disseaparing_t2t7.kill()

                level_2_group.update()
                level_2_group.draw(display_surface)
        
            # collision logic
            # if player_rect.colliderect()
            display_surface.blit(is_paused_button, is_paused_button_rect)

            player_move(player_rect)

        if paused:
            # MENU
            pygame.draw.rect(display_surface,(200,200,200),(menu_topleft[0],menu_topleft[1], 3*WINDOW_WIDTH//5, 2*WINDOW_HEIGHT//4))     
            display_surface.blit(menu_exit_image, menu_exit_rect)


    # display_surface.blit(tow, towrect)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on display_surface

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()