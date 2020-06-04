import pygame
import sys

pygame.init()

game_over = False


player_pos = [700, 500]
player_size = 50

BACKGROUND = (169,169,169)
COLOUR = (255,123,67)
WIDTH = 800
HEIGHT = 600
MOVEMENT_SIZE = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print("key pressed")
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                if x > 0:
                    x = x - MOVEMENT_SIZE
                print("key left: ", x, y)

            elif event.key == pygame.K_RIGHT:
                if x < WIDTH - player_size:
                    x = x + MOVEMENT_SIZE
                print("key right:", x, y)

            elif event.key == pygame.K_DOWN:
                if y < HEIGHT - player_size:
                    y = y + MOVEMENT_SIZE
                print("key down", x, y)

            elif event.key == pygame.K_UP:
                if y > 0:
                    y = y - MOVEMENT_SIZE
                print("key up ", x, y)

            player_pos = [x,y]
            print('foo', flush=True)

    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, COLOUR, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
