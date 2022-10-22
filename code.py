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
main_rect = main_character.get_rect(topleft=(75, 300))

main_title = test_font.render('Game Name', False, 'Yellow')
title_rect = main_title.get_rect(center=(400, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
            # if main_rect.collidepoint(event.pos):
            # print('tão se batendo')

    screen.blit(background, (0, 0))
    screen.blit(tileGrass1, (50, 300))

    pygame.draw.rect(screen, 'Dark Blue', title_rect)
    pygame.draw.rect(screen, 'Dark Blue', title_rect, 10)
    screen.blit(main_title, (title_rect))

    main_rect.left += 3
    if main_rect.left > 800:
        main_rect.right = 0

    # mouse_pos = pygame.mouse.get_pos()
    # if main_rect.collidepoint(mouse_pos):
        # print('ó os cara se batendo sksksksk')

    screen.blit(first_character, (first_char_rect))
    screen.blit(main_character, (main_rect))

    pygame.display.update()
    clock.tick(60)
