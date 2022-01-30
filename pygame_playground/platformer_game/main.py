import pygame
import sys
from level_settings import *
from tiles import Tile

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# test_tile = pygame.sprite.Group(Tile((100, 100), 200))

for row in level_map:
    for str_num in range(len(level_map)):
        global tiles
        if level_map[row][str_num] == 'X':
            tiles += Tile((row*30, str_num*30), 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tiles.draw(screen)

    pygame.display.update()
    clock.tick(60)
