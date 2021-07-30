from random import randint

import pygame
from pygame.locals import *


# Funcao para gerar posicao aleatoria para maca
def on_grid_random():
    x = randint(0, 590)
    y = randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)


# Teste de colisao da snake com a maca
def collision_apple(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

# Montando a snake
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

# Montando a maca
apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

# Direcao que a snake vai startar
my_direction = LEFT

clock = pygame.time.Clock()
fps = 5

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    # Setando fps
    fps = len(snake) * 2 if fps < 30 else 30
    clock.tick(fps)

    # Testando Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        # Testando as teclas pressionadas
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP

            if event.key == K_DOWN:
                my_direction = DOWN

            if event.key == K_LEFT:
                my_direction = LEFT

            if event.key == K_RIGHT:
                my_direction = RIGHT

    # Testando Colisao
    if collision_apple(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score += 1

    # Testando colisao com extremidades e a propria snake
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    # Corpo da snake pegando a posicao da cabeca
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # Mandando a snake para a direcao correta
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)

    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    # Preenchendo a tela com elementos
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)

    score_font = font.render('Score: %s' % (score), True, [255, 255, 255])
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()


while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 0, 0))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 200)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
