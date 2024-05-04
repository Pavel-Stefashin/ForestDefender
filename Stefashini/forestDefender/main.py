import pygame
import random

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((700, 1000))

pygame.display.set_caption("Forest Defender")

icon = pygame.image.load("Stefashini/forestDefender/images/mainIcon.svg")
pygame.display.set_icon(icon)

###### Текст

myfont = pygame.font.Font("Stefashini/forestDefender/fonts/Gugi-Regular.ttf", 40)

text_start_game = myfont.render("Start game", False, (150, 219, 149))
text_start_game_rect = text_start_game.get_rect(topleft=(255, 300))

text_game_over = myfont.render("You lose", False, "Red")

restert_text = myfont.render("Play again", False, "Grey")
restert_text_rect = restert_text.get_rect(topleft=(250, 400))

# Текст


###### Музыка

bg_music = pygame.mixer.Sound("Stefashini/forestDefender/music/Неизвестен — Мелодия флейты - эльфийская песня (www.lightaudio.ru).mp3")

bg_music.play()

# Музыка


###### Окружение

main_ground = pygame.image.load("Stefashini/forestDefender/images/map/ground/ground.png")

forest = pygame.image.load("Stefashini/forestDefender/images/forest_image.svg")

tree = pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/map/trees/tree.png"), (90,130))
christmas_tree = pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/map/trees/tree2.png"), (80,100))

tree_list_in_game = []


# Окружение


###### Враг

enemy_size = (50,70)

enemy_walck_down = [
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/enemy/walck_down/D1.png"), enemy_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/enemy/walck_down/D2.png"), enemy_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/enemy/walck_down/D3.png"), enemy_size)
]

enemy_dath = [
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/enemy/death/D1.png"), enemy_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/enemy/death/D2.png"), enemy_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/enemy/death/D3.png"), enemy_size),
]

enemy_list_in_game = []

enemy_anim_counter = 0
enemy_anim_death_counter = 0

#

###### Кинжал

knife_size = (15, 40)

knife = pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/knife/knife.png"), knife_size)

knife_list_in_game = []

knife_cordinates = []

#

###### Игрок

player_size = (50, 70)

walk_left = [
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/left/L1.png"), player_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/left/L2.png"), player_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/left/L3.png"), player_size)
]

walk_right = [
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/right/R1.png"), player_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/right/R2.png"), player_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/right/R3.png"), player_size)
]

walk_up = [
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/up/U1.png"), player_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/up/U2.png"), player_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/up/U3.png"), player_size),
]

walk_down = [
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/down/D1.png"), player_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/down/D2.png"), player_size),
    pygame.transform.scale(pygame.image.load("Stefashini/forestDefender/images/sprite_elf/down/D3.png"), player_size)
]

player_anim_counter = 0

player_cordinates = [300, 650]

# Игрок

back_ground_y = 0

tree_timer = pygame.USEREVENT + 1
pygame.time.set_timer(tree_timer, 1000)

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 4000)

knife_timer = pygame.USEREVENT + 1
pygame.time.set_timer(knife_timer, 1500)

knife_cordinates = player_cordinates

gameplay = 0

running = True

points = 0
points_font = pygame.font.Font("Stefashini/forestDefender/fonts/Gugi-Regular.ttf", 20)


while running:

    screen.blit(main_ground, (0, back_ground_y))
    screen.blit(main_ground, (0, back_ground_y - 1000))

    if gameplay == 0:
        screen.fill((43, 171, 41))
        screen.blit(text_start_game, text_start_game_rect)

        mouse_position = pygame.mouse.get_pos()
        if text_start_game_rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            gameplay = 1
    elif gameplay == 1: 
        player_rect = walk_down[0].get_rect(topleft = player_cordinates)

        points += 1

        if tree_list_in_game:
            for el in tree_list_in_game:
                screen.blit(tree, el)
                el.y += 5

                if el.y > 1000:
                    tree_list_in_game.remove(el)  

                if player_rect.colliderect(el):
                    gameplay = 2
                
                if knife_list_in_game:
                    for (index_knife, knife_el) in enumerate(knife_list_in_game):

                        if knife_el.colliderect(el):
                            knife_list_in_game.pop(index_knife)

        if enemy_list_in_game:
            for (index_enemy, enemy_el) in enumerate(enemy_list_in_game):

                if knife_list_in_game:
                    for (index_knife, knife_el) in enumerate(knife_list_in_game):

                        if knife_el.colliderect(enemy_el):
                            enemy_list_in_game.pop(index_enemy)
                            knife_list_in_game.pop(index_knife)
                            points += 100
                        
                screen.blit(enemy_walck_down[enemy_anim_counter], enemy_el)
                enemy_el.y += 10

                if enemy_el.y > 1000:
                    enemy_list_in_game.pop(index_enemy)  

                if player_rect.colliderect(enemy_el):
                    gameplay = 2

        if knife_list_in_game:
            for (index_knife, kn) in enumerate(knife_list_in_game):
                screen.blit(knife, kn)
                kn.y -= 40

            if kn.y < 0:
                knife_list_in_game.remove(kn)  

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_cordinates[0] > 0:
            screen.blit(walk_left[player_anim_counter], player_cordinates)
            player_anim_counter += 1
            player_cordinates[0] -= 10
        elif keys[pygame.K_d] and player_cordinates[0] < screen.get_width() - 70:
            screen.blit(walk_right[player_anim_counter], player_cordinates)
            player_anim_counter += 1
            player_cordinates[0] += 10
        elif keys[pygame.K_w] and player_cordinates[1] > 0:
            screen.blit(walk_up[player_anim_counter], player_cordinates)
            player_anim_counter += 1
            player_cordinates[1] -= 10
        elif keys[pygame.K_s] and player_cordinates[1] < screen.get_height() - 100:
            screen.blit(walk_up[player_anim_counter], player_cordinates)
            player_anim_counter += 1
            player_cordinates[1] += 10
        else:
            screen.blit(walk_up[player_anim_counter], player_cordinates)
            player_anim_counter += 1

        if player_anim_counter == 2:
            player_anim_counter = 0

        back_ground_y += 5
        if back_ground_y == 1000:
            back_ground_y = 0
        
        text_points = points_font.render("Your poits: " + str(points), False, "White")
        screen.blit(text_points, (550, 30))
        
    elif gameplay == 2:
        screen.fill((87, 88, 89))
        screen.blit(text_game_over, (255, 300))
        screen.blit(restert_text, restert_text_rect)
        text_points = points_font.render("Your result: " + str(points), False, "White")
        screen.blit(text_points, (280, 700))

        mouse_position = pygame.mouse.get_pos()
        if restert_text_rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            gameplay = 1
            player_cordinates = [300, 650]
            enemy_list_in_game.clear()
            knife_list_in_game.clear()
            tree_list_in_game.clear()
            points = 0


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        for i in range(random.randint(1, 5)):
            if event.type == tree_timer:
                tree_list_in_game.append(tree.get_rect(topleft=(random.randint(50, 650), random.randint(-800, -200))))
                pygame.time.set_timer(tree_timer, random.randint(2000, 5000))
        for i in range(random.randint(1, 3)):
            if event.type == enemy_timer:
                enemy_list_in_game.append(enemy_walck_down[0].get_rect(topleft=(random.randint(50, 650), random.randint(-800, -200))))
                pygame.time.set_timer(enemy_timer, random.randint(2000, 7000))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            knife_list_in_game.append(knife.get_rect(topleft=(knife_cordinates[0] + 17, knife_cordinates[1] + 25)))    


    clock.tick(15)

    enemy_anim_counter += 1

    if enemy_anim_counter == 2:
        enemy_anim_counter = 0

    knife_cordinates = player_cordinates