import pygame
import sys

pygame.init()

game_over = False


player_pos = [700, 500]
player_size = 50

COLOUR = (255,123,67)
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print("key down")
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                print("key left")
                x = x - player_size
            elif event.key == pygame.K_RIGHT:
                print("key right")
                x = x + player_size

            elif event.key == pygame.K_DOWN:
                print("key down ")
                x = x + player_size

            player_pos = [x,y]

    pygame.draw.rect(screen, COLOUR, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
