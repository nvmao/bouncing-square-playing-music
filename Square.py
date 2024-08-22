import random
import pygame
from pygame import Vector2

from utils import utils


class Square:
    def __init__(self, pos, width=50, color=(255, 255, 255)):
        self.color = color
        self.width = width
        self.pos = pos
        self.vel = Vector2(550, 800)
        self.trail = []  # List to store the trail positions
        self.trail_lifetime = 10  # Number of frames the trail lasts

    def getRect(self):
        return pygame.Rect(self.pos.x,self.pos.y,self.width,self.width)

    def update(self,deltaTime):
        self.trail.append(self.pos.copy())  # Store the current position in the trail
        if len(self.trail) > self.trail_lifetime:
            self.trail.pop(0)  # Remove the oldest position if we've reached the max length
        self.pos += self.vel * deltaTime


    def draw(self,camera):
        # Draw the trail
        hue = 0
        hueStep = 1 / len(self.trail)
        for i, pos in enumerate(reversed(self.trail)):
            # Calculate the size and opacity based on the index in the trail
            size_factor = 1 - (i / self.trail_lifetime)  # Gradually decrease size
            current_width = self.width * size_factor  # Scale the width
            alpha = 255 * (1 - i / self.trail_lifetime)  # Fade out effect

            # Create a color with alpha
            color = utils.hueToRGB(hue)
            hue += hueStep
            color_with_alpha = (color[0], color[1], color[2], alpha)
            # Draw a smaller rectangle for the trail
            pos = camera.apply_pos(pos)
            pygame.draw.rect(utils.screen, color_with_alpha,
                             (pos.x, pos.y ,
                              current_width, current_width))

        # Draw the square itself
        pos = camera.apply_pos(self.pos)
        pygame.draw.rect(utils.screen, self.color,
                         (pos.x, pos.y ,
                          self.width, self.width))
