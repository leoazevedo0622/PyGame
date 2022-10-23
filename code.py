from sys import exit

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game Name')
clock = pygame.time.Clock()

test_font = pygame.font.Font('fonts/SHPinscher-Regular.otf', 50)


background = pygame.image.load('graphics/background2.png').convert()

tileGrass1 = pygame.image.load('graphics/platforms/grass1.png').convert()

first_character = pygame.image.load(
    'graphics/characters/agent.png').convert_alpha()
first_char_rect = first_character.get_rect(topleft=(350, 300))

main_character = pygame.image.load(
    'graphics/characters/tile000.png').convert_alpha()
main_rect = main_character.get_rect(bottomleft=(75, 300))
player_grav = 0

main_title = test_font.render('Game Name', False, '#E9D5D8')
title_rect = main_title.get_rect(center=(400, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_rect.collidepoint(event.pos):
                player_grav = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_grav = -20

    screen.blit(background, (0, 0))
    screen.blit(tileGrass1, (50, 270))

    pygame.draw.rect(screen, '#52ABE6', title_rect)
    pygame.draw.rect(screen, '#52ABE6', title_rect, 10)
    screen.blit(main_title, (title_rect))

    screen.blit(first_character, (first_char_rect))

    # Player
    player_grav += 1
    main_rect.y += player_grav
    if main_rect.bottom >= 300:
        main_rect.bottom = 300
    screen.blit(main_character, (main_rect))

    pygame.display.update()
    clock.tick(60)
