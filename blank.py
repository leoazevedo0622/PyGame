from sys import exit

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Rage Square')
clock = pygame.time.Clock()

test_font = pygame.font.Font('fonts/SHPinscher-Regular.otf', 50)

background = pygame.image.load('graphics/background1.png')
first_character = pygame.image.load('graphics/characters/agent.png')
text_font = test_font.render('Game Name', False, 'Yellow')

char_xPos = 350
char_yPos = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(text_font, (300, 50))

    if char_xPos > 500 and char_yPos < -100:
        char_xPos = -50
        char_yPos = 400

    char_xPos += 2
    char_yPos -= 1
    screen.blit(first_character, (char_xPos, char_yPos))

    pygame.display.update()
    clock.tick(60)
