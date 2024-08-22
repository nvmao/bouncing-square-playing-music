import pygame
from pygame import Vector2, Rect

from utils import utils


class Camera:
    def __init__(self, width, height):
        self.camera = Vector2(0, 0)
        self.width = width
        self.height = height
        self.smooth_speed = 2  # Adjust this value to control how smooth the camera movement is
        self.target = None

    def set_target(self, target):
        self.target = target

    def apply_pos(self, pos):
        offset = -self.camera + Vector2(utils.width/2, utils.height/2)
        # Offset the entity's position by the camera position to get the correct rendering position
        return Vector2(pos.x +offset.x,pos.y + offset.y)


    def update(self):
        if not self.target:
            return
        target_pos = Vector2(self.target.getRect().center)
        heading = target_pos - self.camera
        self.camera += heading * self.smooth_speed * utils.deltaTime()



