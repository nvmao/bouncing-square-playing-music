import pygame
from utils import utils

from Game import Game

game = Game()

while True:
    utils.screen.fill((249, 219, 186), (0, 0, utils.width, utils.height))
    utils.initDeltaTime()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    game.update()
    game.draw()


    pygame.display.flip()


