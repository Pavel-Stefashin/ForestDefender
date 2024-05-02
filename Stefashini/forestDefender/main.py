import pygame

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((1000, 700))

pygame.display.set_caption("Forest Defender")

back_glade = pygame.image.load("images/glade2.png")

icon = pygame.image.load("images/mainIcon.svg")
pygame.display.set_icon(icon)

forest = pygame.image.load("images/forest_image.svg")

player = pygame.image.load("images/sprite_elf/left/L1.png")

walk_left = [
    pygame.image.load("images/sprite_elf/left/L1.png"),
    pygame.image.load("images/sprite_elf/left/L2.png"),
    pygame.image.load("images/sprite_elf/left/L3.png")
]

walk_right = [
    pygame.image.load("images/sprite_elf/right/R1.png"),
    pygame.image.load("images/sprite_elf/right/R2.png"),
    pygame.image.load("images/sprite_elf/right/R3.png")
]

walk_up = [
    pygame.image.load("images/sprite_elf/up/U1.png"),
    pygame.image.load("images/sprite_elf/up/U2.png"),
    pygame.image.load("images/sprite_elf/up/U3.png")
]

walk_down = [
    pygame.image.load("images/sprite_elf/down/D1.png"),
    pygame.image.load("images/sprite_elf/down/D2.png"),
    pygame.image.load("images/sprite_elf/down/D3.png")
]

player_anim_counter = 0

cordinates = {'x': 500, 'y': 350}

running = True
while running:

    screen.blit(back_glade, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_counter], (cordinates['x'], cordinates['y']))
        player_anim_counter += 1
        cordinates['x'] -= 10
    elif keys[pygame.K_d]:
        screen.blit(walk_right[player_anim_counter], (cordinates['x'], cordinates['y']))
        player_anim_counter += 1
        cordinates['x'] += 10
    elif keys[pygame.K_w]:
        screen.blit(walk_up[player_anim_counter], (cordinates['x'], cordinates['y']))
        player_anim_counter += 1
        cordinates['y'] -= 10
    elif keys[pygame.K_s]:
        screen.blit(walk_down[player_anim_counter], (cordinates['x'], cordinates['y']))
        player_anim_counter += 1
        cordinates['y'] += 10
    else:
        screen.blit(walk_down[0], (cordinates['x'], cordinates['y']))

    if player_anim_counter == 2:
        player_anim_counter = 0
    pygame.display.update()
    clock.tick(15)

