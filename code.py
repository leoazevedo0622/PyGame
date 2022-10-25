from sys import exit

import pygame


def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(
        f'Score: {current_time}', False, '#E9D5D8')
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game Name')
clock = pygame.time.Clock()
game_active = True
start_time = 0

test_font = pygame.font.Font('fonts/SHPinscher-Regular.otf', 50)


background = pygame.image.load('graphics/background2.png').convert()

tileGrass1 = pygame.image.load('graphics/platforms/grass1.png').convert()

first_character = pygame.image.load(
    'graphics/characters/enemy_1.png').convert_alpha()
first_char_rect = first_character.get_rect(topleft=(350, 314))

main_character = pygame.image.load(
    'graphics/characters/tile000.png').convert_alpha()
main_rect = main_character.get_rect(bottomleft=(75, 364))
player_grav = 0

# main_title = test_font.render('Corre Walter!', False, '#E9D5D8')
#title_rect = main_title.get_rect(center=(400, 50))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_rect.collidepoint(event.pos) and main_rect.bottom == 365:
                    player_grav = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and main_rect.bottom == 365:
                    player_grav = -20

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    first_char_rect.left = 800
                    start_time = int(pygame.time.get_ticks()/1000)

    if game_active:

        screen.blit(background, (0, 0))
        screen.blit(tileGrass1, (-60, 336))
        screen.blit(tileGrass1, (0, 336))
        screen.blit(tileGrass1, (90, 336))
        screen.blit(tileGrass1, (180, 336))
        screen.blit(tileGrass1, (270, 336))
        screen.blit(tileGrass1, (360, 336))
        screen.blit(tileGrass1, (450, 336))
        screen.blit(tileGrass1, (540, 336))
        screen.blit(tileGrass1, (630, 336))
        screen.blit(tileGrass1, (720, 336))

        # pygame.draw.rect(screen, '#52ABE6', title_rect)
        # pygame.draw.rect(screen, '#52ABE6', title_rect, 10)
        # screen.blit(main_title, (title_rect))

        first_char_rect.left -= 5
        if first_char_rect.right <= 0:
            first_char_rect.left = 800
        screen.blit(first_character, (first_char_rect))

        # Player
        player_grav += 1
        main_rect.y += player_grav
        if main_rect.bottom >= 365:
            main_rect.bottom = 365
        screen.blit(main_character, (main_rect))

        # Collision with Enemy
        if first_char_rect.colliderect(main_rect):
            game_active = False

        display_score()

    else:
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)
