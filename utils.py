import colorsys

import pygame

from pygame.locals import *

from pygame import time
import pygame.midi


# a global class
# store global variable, functions

class Utils():

    def __init__(self):

        pygame.init()

        self.width = 1280
        self.height = 1280

        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF, 16)
        self.dt = 0
        self.clock = pygame.time.Clock()

        pygame.midi.init()
        self.volumeScale = 10
        self.player = pygame.midi.Output(0)

    def initDeltaTime(self):  # calculate deltaTime
        t = self.clock.tick(60)
        self.dt = t / 1000

    def deltaTime(self):
        return self.dt

    def hueToRGB(self, hue):
        # Convert HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        # Scale RGB values to 0-255 range
        return (int(r * 255), int(g * 255), int(b * 255))


utils = Utils()  # util is global object
