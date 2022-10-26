from random import randint
from sys import exit

import pygame


def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(
        f'Score: {current_time}', False, '#E9D5D8')
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


def enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.x -= 5

            if enemy_rect.bottom == 364:
                screen.blit(first_character, enemy_rect)
            else:
                screen.blit(enemy2_character, enemy_rect)

        enemy_list = [enemy for enemy in enemy_list if enemy.x > -100]

        return enemy_list
    else:
        return []


def collisions(player, enemies):
    if enemies:
        for enemy_rect in enemies:
            if player.colliderect(enemy_rect):
                return False
    return True


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game Name')
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0

test_font = pygame.font.Font('fonts/SHPinscher-Regular.otf', 50)

game_title_surf = test_font.render('Corre Walter', False, '#ec0909')
game_title_rect = game_title_surf.get_rect(center=(400, 120))

jump_control = test_font.render('Press Space To Jump', False, '#ec0909')
jump_control_rect = jump_control.get_rect(center=(400, 300))

background = pygame.image.load('graphics/background2.png').convert()

tileGrass1 = pygame.image.load('graphics/platforms/grass1.png').convert()


first_character = pygame.image.load(
    'graphics/characters/enemy_1.png').convert_alpha()
enemy2_character = pygame.image.load(
    'graphics/characters/enemy_2.png').convert_alpha()


enemy_rect_list = []


main_character = pygame.image.load(
    'graphics/characters/tile000.png').convert_alpha()
main_rect = main_character.get_rect(midbottom=(75, 364))

menu_player = pygame.image.load(
    'graphics/characters/tile000.png').convert_alpha()
menu_player = pygame.transform.rotozoom(menu_player, 0, 2)
menu_player_rect = menu_player.get_rect(center=(400, 200))

player_grav = 0

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

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
                    start_time = int(pygame.time.get_ticks()/1000)

        if event.type == obstacle_timer and game_active:
            if (randint(0, 2)):
                enemy_rect_list.append(first_character.get_rect(
                    bottomleft=(randint(900, 1100), 364)))
            else:
                enemy_rect_list.append(enemy2_character.get_rect(
                    bottomleft=(randint(900, 1100), 290)))

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

        # first_char_rect.left -= 5
        # if first_char_rect.right <= 0:
        # first_char_rect.left = 800
        # screen.blit(first_character, (first_char_rect))

        # Player
        player_grav += 1
        main_rect.y += player_grav
        if main_rect.bottom >= 365:
            main_rect.bottom = 365

        screen.blit(main_character, (main_rect))

        enemy_rect_list = enemy_movement(enemy_rect_list)

        # Collision with Enemy
        game_active = collisions(main_rect, enemy_rect_list)

        score = display_score()

    else:
        screen.fill('#5355ac')
        screen.blit(menu_player, (menu_player_rect))
        enemy_rect_list.clear()
        main_rect.midbottom = (75, 364)
        player_grav = 0

        your_score = test_font.render(f'Your Score: {score}', False, '#ec0909')
        your_score_rect = your_score.get_rect(center=(400, 300))
        if score == 0:
            screen.blit(jump_control, (jump_control_rect))
        else:
            screen.blit(your_score, (your_score_rect))

        screen.blit(game_title_surf, (game_title_rect))

    pygame.display.update()
    clock.tick(60)
